# Cloud Quest
## 01 Cloud Practitioner

------

[...]

### 3. Networking Concepts - Banking Headquarters

- In AWS, by default, VPCs (Virtual Private Cloud) are configured with internet gateways and routing to the internet. When you create a new VPC, you can choose whether all or part of the VPC should be exposed to the internet.

![alt text](image_vpc.png)

- NACL (Network Access Control List) is a stateless firewall that controls traffic in and out of one or more subnets. It is a list of rules that allow or deny traffic based on IP addresses, protocols, and ports.

- Security Groups are stateful firewalls that control traffic in and out of one or more instances. They are associated with instances and are evaluated before NACLs.

- Route Tables are used to determine where network traffic is directed. They are associated with subnets and are evaluated after NACLs.

- Subnets are a range of IP addresses in your VPC. They are associated with a single availability zone and a single route table.

- Internet Gateways are used to allow traffic to and from the internet. They are associated with a VPC and are used to route traffic to and from the internet.

- NAT Gateways are used to allow instances in a private subnet to access the internet. They are associated with a public subnet and are used to route traffic to and from the internet.

- EC2 instances can be provided with Temporary block level storage called Instance Store Volumes. These volumes are deleted when the instance is stopped or terminated. Thay can alos be attached to an EBS (Elastic Block Store) volume which is persistent storage.

- AMIs (Amazon Machine Images) are used to create EC2 instances. They are templates that contain the software configuration (OS, application server, and applications) required to launch an instance. They can be stored in S3.

- EFS (Elastic File System) is a scalable file storage service that can be used to store files that are accessed by multiple EC2 instances.