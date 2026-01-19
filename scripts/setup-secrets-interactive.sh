#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Arrays to store collected secrets and selected stages
declare -a SELECTED_STAGES=()
declare -a SECRET_KEYS=()
declare -a SECRET_VALUES=()

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}  SST Secrets Configuration Setup${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""

# Function to select stages interactively
select_stages() {
    echo -e "${YELLOW}Select stages to configure:${NC}"
    echo -e "${NC}(Enter numbers separated by spaces, e.g., '1 2' for dev and prod)${NC}"
    echo ""
    echo "  1) dev"
    echo "  2) prod"
    echo "  3) production"
    echo "  4) adam"
    echo "  5) justme"
    echo ""
    read -p "Enter your choices: " stage_choices

    if [ -z "$stage_choices" ]; then
        echo -e "${RED}No stages selected. Exiting.${NC}"
        exit 1
    fi

    for choice in $stage_choices; do
        case $choice in
            1) SELECTED_STAGES+=("dev") ;;
            2) SELECTED_STAGES+=("prod") ;;
            3) SELECTED_STAGES+=("production") ;;
            4) SELECTED_STAGES+=("adam") ;;
            5) SELECTED_STAGES+=("justme") ;;
            *)
                echo -e "${RED}Invalid choice: $choice (skipping)${NC}"
                ;;
        esac
    done

    if [ ${#SELECTED_STAGES[@]} -eq 0 ]; then
        echo -e "${RED}No valid stages selected. Exiting.${NC}"
        exit 1
    fi

    echo ""
    echo -e "${GREEN}Selected stages: ${SELECTED_STAGES[*]}${NC}"
    echo ""
}

# Function to collect a secret
collect_secret() {
    local secret_key=$1
    local secret_name=$2
    local secret_description=$3
    local example=$4

    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}${secret_name}${NC}"
    echo -e "${NC}${secret_description}${NC}"

    if [ ! -z "$example" ]; then
        echo -e "${NC}Example: ${YELLOW}${example}${NC}"
    fi

    echo -e "${NC}(Press Enter to skip)${NC}"
    echo ""

    # Read secret value (hidden input for sensitive data)
    read -s -p "Enter value: " secret_value
    echo ""

    # Skip if empty
    if [ -z "$secret_value" ]; then
        echo -e "${YELLOW}Skipped${NC}"
        return
    fi

    # Store the secret in parallel arrays
    SECRET_KEYS+=("$secret_key")
    SECRET_VALUES+=("$secret_value")
    echo -e "${GREEN}Collected${NC}"
}

# Function to apply all secrets
apply_secrets() {
    local total_operations=$((${#SECRET_KEYS[@]} * ${#SELECTED_STAGES[@]}))
    local current=0

    echo ""
    echo -e "${BLUE}=====================================${NC}"
    echo -e "${BLUE}  Applying Secrets${NC}"
    echo -e "${BLUE}=====================================${NC}"
    echo ""
    echo -e "${NC}Total operations: ${total_operations}${NC}"
    echo ""

    for stage in "${SELECTED_STAGES[@]}"; do
        echo -e "${CYAN}Stage: ${stage}${NC}"
        echo -e "${CYAN}─────────────────────${NC}"

        for i in "${!SECRET_KEYS[@]}"; do
            current=$((current + 1))
            secret_key="${SECRET_KEYS[$i]}"
            secret_value="${SECRET_VALUES[$i]}"

            echo -ne "  [${current}/${total_operations}] Setting ${secret_key}... "

            if sst secret set "$secret_key" "$secret_value" --stage "$stage" 2>/dev/null; then
                echo -e "${GREEN}Done${NC}"
            else
                echo -e "${RED}Failed${NC}"
                echo -e "${RED}Error setting ${secret_key} for stage ${stage}${NC}"
                read -p "Continue anyway? (y/n): " continue_choice
                if [ "$continue_choice" != "y" ] && [ "$continue_choice" != "Y" ]; then
                    exit 1
                fi
            fi
        done

        echo ""
    done
}

# Main script
echo -e "${NC}This script will help you configure all required secrets for your SST application.${NC}"
echo -e "${NC}First, select stages. Then enter all secret values. Finally, secrets will be applied.${NC}"
echo ""

# Step 1: Select stages
select_stages

# Confirmation
echo -e "${YELLOW}You are about to configure secrets for: ${SELECTED_STAGES[*]}${NC}"
read -p "Continue? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo -e "${RED}Aborted.${NC}"
    exit 0
fi

echo ""
echo -e "${GREEN}Step 1/3: Collecting secrets (press Enter to skip any)...${NC}"
echo ""

# Collect secrets (all can be skipped)
collect_secret "DB_URL" \
    "Database URL" \
    "PostgreSQL connection string with pgvector extension enabled" \
    "postgresql://user:pass@host:5432/dbname"

collect_secret "BETTER_AUTH_SECRET" \
    "Better Auth Secret" \
    "Secret key for Better Auth session encryption (generate with: openssl rand -base64 32)" \
    "K7dF9sL2mN4pQ8rT1vX3yZ6aB0cE5gH..."

collect_secret "OPENAI_API_KEY" \
    "OpenAI API Key" \
    "API key for embeddings and AI-powered features" \
    "sk-proj-..."

collect_secret "RESEND_API_KEY" \
    "Resend API Key" \
    "API key for sending emails via Resend" \
    "re_..."

echo ""
echo -e "${GREEN}Step 2/3: OAuth configuration...${NC}"
echo ""

# GitHub OAuth
echo -e "${YELLOW}Configure GitHub OAuth? (y/n):${NC}"
read -p "" setup_github

if [ "$setup_github" = "y" ] || [ "$setup_github" = "Y" ]; then
    collect_secret "GITHUB_CLIENT_ID" \
        "GitHub Client ID" \
        "GitHub OAuth App Client ID (from https://github.com/settings/developers)" \
        "Iv1.abc123..."

    collect_secret "GITHUB_CLIENT_SECRET" \
        "GitHub Client Secret" \
        "GitHub OAuth App Client Secret" \
        ""
fi

# Google OAuth
echo ""
echo -e "${YELLOW}Configure Google OAuth? (y/n):${NC}"
read -p "" setup_google

if [ "$setup_google" = "y" ] || [ "$setup_google" = "Y" ]; then
    collect_secret "GOOGLE_CLIENT_ID" \
        "Google Client ID" \
        "Google OAuth Client ID (from Google Cloud Console)" \
        "123456789-abc.apps.googleusercontent.com"

    collect_secret "GOOGLE_CLIENT_SECRET" \
        "Google Client Secret" \
        "Google OAuth Client Secret" \
        "GOCSPX-..."
fi

echo ""
echo -e "${GREEN}Step 3/3: Applying secrets to selected stages...${NC}"

# Check if any secrets were collected
if [ ${#SECRET_KEYS[@]} -eq 0 ]; then
    echo ""
    echo -e "${YELLOW}No secrets were provided. Nothing to apply.${NC}"
    exit 0
fi

# Show summary before applying
echo ""
echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}  Summary${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""
echo -e "${NC}Stages: ${CYAN}${SELECTED_STAGES[*]}${NC}"
echo -e "${NC}Secrets to set:${NC}"
for secret_key in "${SECRET_KEYS[@]}"; do
    echo -e "  - ${secret_key}"
done
echo ""

read -p "Apply these secrets? (y/n): " apply_confirm

if [ "$apply_confirm" != "y" ] && [ "$apply_confirm" != "Y" ]; then
    echo -e "${RED}Aborted.${NC}"
    exit 0
fi

# Apply all secrets
apply_secrets

# Success message
echo -e "${BLUE}=====================================${NC}"
echo -e "${GREEN}All secrets configured successfully!${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""
echo -e "${NC}Next steps:${NC}"
echo -e "1. Run migrations: ${YELLOW}pnpm --filter @starter/core db:migrate:local${NC}"
echo -e "2. Start development: ${YELLOW}pnpm dev${NC}"
echo ""
echo -e "${NC}To view your secrets, run:${NC}"
for stage in "${SELECTED_STAGES[@]}"; do
    echo -e "  ${YELLOW}sst secret list --stage ${stage}${NC}"
done
echo ""
