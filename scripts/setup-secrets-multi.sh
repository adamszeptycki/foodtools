#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Array to hold selected stages
STAGES=()

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}  SST Secrets Configuration Setup${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""

# Function to prompt for stage
select_stage() {
    echo -e "${YELLOW}Select the stage(s) to configure:${NC}"
    echo "1) adam"
    echo "2) prod"
    echo "3) both (adam + prod)"
    echo ""
    read -p "Enter your choice (1-3): " stage_choice

    case $stage_choice in
        1)
            STAGES=("adam")
            ;;
        2)
            STAGES=("prod")
            ;;
        3)
            STAGES=("adam" "prod")
            ;;
        *)
            echo -e "${RED}Invalid choice. Please run the script again.${NC}"
            exit 1
            ;;
    esac

    echo -e "${GREEN}Selected stage(s): ${STAGES[*]}${NC}"
    echo ""
}

# Function to set a secret for all selected stages
set_secret() {
    local secret_name=$1
    local secret_description=$2
    local is_optional=$3
    local example=$4

    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Secret: ${secret_name}${NC}"
    echo -e "${NC}${secret_description}${NC}"

    if [ ! -z "$example" ]; then
        echo -e "${CYAN}Example: ${example}${NC}"
    fi

    if [ "$is_optional" = true ]; then
        echo -e "${NC}(Optional - press Enter to skip)${NC}"
    fi

    echo ""

    # Read secret value (hidden input)
    read -s -p "Enter value: " secret_value
    echo ""

    # Skip if optional and empty
    if [ "$is_optional" = true ] && [ -z "$secret_value" ]; then
        echo -e "${YELLOW}Skipped ${secret_name}${NC}"
        echo ""
        return
    fi

    # Validate that required secrets are not empty
    if [ -z "$secret_value" ]; then
        echo -e "${RED}Error: ${secret_name} is required and cannot be empty${NC}"
        echo ""
        exit 1
    fi

    # Set the secret for each selected stage
    for stage in "${STAGES[@]}"; do
        echo -e "${NC}Setting secret for stage: ${stage}...${NC}"
        if sst secret set "$secret_name" "$secret_value" --stage "$stage"; then
            echo -e "${GREEN}✓ Successfully set ${secret_name} for ${stage}${NC}"
        else
            echo -e "${RED}✗ Failed to set ${secret_name} for ${stage}${NC}"
            exit 1
        fi
    done

    echo ""
}

# Main script
echo -e "${NC}This script will help you configure all required secrets for your SST application.${NC}"
echo -e "${NC}You can set secrets for one stage or both stages at once.${NC}"
echo ""

# Select stage
select_stage

# Confirmation
echo -e "${YELLOW}You are about to configure secrets for: ${STAGES[*]}${NC}"
read -p "Continue? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo -e "${RED}Aborted.${NC}"
    exit 0
fi

echo ""
echo -e "${GREEN}Starting secrets configuration...${NC}"
echo ""

# Set required secrets
set_secret "OPENAI_API_KEY" \
    "OpenAI API key for AI-powered features (embeddings and structured data extraction)" \
    false \
    "sk-proj-..."

set_secret "BETTER_AUTH_SECRET" \
    "Secret key for Better Auth session encryption (generate a random 32+ character string)" \
    false \
    "Use: openssl rand -base64 32"

# Set optional secrets
set_secret "DATABASE_URL" \
    "PostgreSQL connection string with pgvector extension enabled" \
    true \
    "postgresql://user:pass@host:5432/dbname"

# Optional: GitHub OAuth
echo -e "${YELLOW}Do you want to configure GitHub OAuth? (y/n):${NC}"
read -p "" setup_github

if [ "$setup_github" = "y" ] || [ "$setup_github" = "Y" ]; then
    set_secret "GITHUB_CLIENT_ID" \
        "GitHub OAuth App Client ID (from https://github.com/settings/developers)" \
        true \
        "Iv1.abc123..."

    set_secret "GITHUB_CLIENT_SECRET" \
        "GitHub OAuth App Client Secret" \
        true \
        "abc123..."
fi

# Optional: Google OAuth
echo -e "${YELLOW}Do you want to configure Google OAuth? (y/n):${NC}"
read -p "" setup_google

if [ "$setup_google" = "y" ] || [ "$setup_google" = "Y" ]; then
    set_secret "GOOGLE_CLIENT_ID" \
        "Google OAuth Client ID (from Google Cloud Console)" \
        true \
        "123456789-abc.apps.googleusercontent.com"

    set_secret "GOOGLE_CLIENT_SECRET" \
        "Google OAuth Client Secret" \
        true \
        "GOCSPX-..."
fi

# Success message
echo -e "${BLUE}=====================================${NC}"
echo -e "${GREEN}✓ All secrets configured successfully!${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""
echo -e "${NC}Secrets were set for: ${CYAN}${STAGES[*]}${NC}"
echo ""
echo -e "${NC}To view your secrets, run:${NC}"
for stage in "${STAGES[@]}"; do
    echo -e "  ${YELLOW}sst secret list --stage ${stage}${NC}"
done
echo ""
echo -e "${NC}Next steps:${NC}"
echo -e "1. Run migrations: ${YELLOW}pnpm --filter @foodtools/core db:migrate:local${NC}"
echo -e "2. Start development: ${YELLOW}pnpm dev${NC}"
echo ""
