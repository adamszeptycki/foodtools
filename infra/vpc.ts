export const vpc = new sst.aws.Vpc("FoodToolsVpc", {
	bastion: true, // For direct DB access during migrations
	nat: "ec2", // Cost-effective NAT for outbound traffic
});
