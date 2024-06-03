# Postmortem Report: Outage on MyWebApp Service

![Outage Diagram](https://drive.usercontent.google.com/download?id=1Hxsf92EAfjgTMISAEUPlnRR2zih6kwgI&authuser=0)

## Issue Summary
**Duration:** May 28, 2024, 14:00 - 16:00 UTC (2 hours)  
**Impact:** The MyWebApp service experienced a significant slowdown. Users encountered slow page loads and occasional timeouts. Approximately 70% of users were affected.  
**Root Cause:** A misconfiguration in the Nginx load balancer caused inefficient routing, leading to an overload on one of the backend servers.

## Timeline
- **14:00 UTC:** Issue detected by automated monitoring alert indicating an increase in page load times and timeouts.
- **14:05 UTC:** Initial investigation by the on-call engineer; confirmed issue through user reports and logs.
- **14:10 UTC:** Assumed root cause to be a sudden spike in traffic.
- **14:20 UTC:** Misleading investigation into traffic patterns, found no unusual spikes.
- **14:30 UTC:** Escalated to the DevOps team for further analysis.
- **15:00 UTC:** DevOps team identified an imbalance in traffic distribution due to a misconfiguration in the Nginx load balancer.
- **15:15 UTC:** Applied temporary fix by correcting the load balancer configuration.
- **15:45 UTC:** Verified resolution; service performance returned to normal and monitored for stability.
- **16:00 UTC:** Declared incident resolved after ensuring consistent performance.

## Root Cause and Resolution
**Root Cause:**  
The Nginx load balancer configuration was manually edited during a routine update, introducing an error that caused it to route most traffic to a single backend server. This resulted in an overload on that server, causing slowdowns and timeouts for users.

**Resolution:**  
The issue was resolved by correcting the Nginx configuration to ensure even distribution of traffic across all backend servers. The corrected configuration was tested and validated before being deployed. Monitoring confirmed that the traffic was evenly distributed and the service performance was stable.

## Corrective and Preventative Measures
**Improvements:**
1. **Automate Configuration Management:** Implement tools like Ansible or Puppet to manage Nginx configurations, reducing the risk of manual errors.
2. **Enhanced Monitoring:** Increase monitoring granularity for the load balancer to detect configuration issues quickly.
3. **Deploy Review Process:** Establish a peer review process for configuration changes before deployment.

**Tasks:**
1. Implement automated configuration management for Nginx using Ansible.
2. Add detailed monitoring for Nginx configuration and routing errors.
3. Create a deployment checklist that includes configuration validation steps.
4. Conduct training sessions for the team on best practices for configuration changes and deployment.
5. Hold a post-incident review meeting to ensure lessons learned are communicated and incorporated into standard procedures.

## A Bit of Humor
We all know how it feels when things go wrong:

![Funny Meme]()

By implementing these measures, we aim to prevent similar outages and ensure a more robust and resilient service.

