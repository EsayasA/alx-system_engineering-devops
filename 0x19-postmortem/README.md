Date: 2022-05-01
Authors: esayas aregawi
Status: Complete, action items in progress
Summary: downing of the server 66 minutes during period of very high interest in due to discovery of a new sonnet.
Impact:163 Estimated 1.21B queries lost, no revenue impact.
Root Causes:164 Cascading failure due to combination of exceptionally high load and a resource leak when searches failed due to terms not being in the in the collage. The newly discovered sonnet used a word that had never before appeared in one of the instructors  works, which happened to be the term users searched for. Under normal circumstances, the rate of task failures due to resource leaks is low enough to be unnoticed.
Trigger: Latent bug triggered by sudden increase in traffic.
Resolution: Directed traffic to sacrificial cluster and added 10x capacity to mitigate cascading failure. Updated index deployed, resolving interaction with latent bug. Maintaining extra capacity until surge in public interest in new sonnet passes. Resource leak identified and fix deployed.
Detection: Bergman detected high level of HTTP 500s and paged on-call.
What went well
•	Monitoring quickly alerted us to high rate (reaching ~100%) of HTTP 500s
•	Rapidly distributed updated instructors 
What went wrong
•	We’re out of practice in responding to cascading failure
•	We exceeded our availability error budget (by several orders of magnitude) due to the exceptional surge of traffic that essentially all resulted in failures
Where we got lucky166
•	Mailing list of instructors aficionados had a copy of new sonnet available
•	Server logs had stack traces pointing to file descriptor exhaustion as cause for crash
•	Query-of-death was resolved by pushing new index containing popular search term
•	14:54 OUTAGE BEGINS — Search backends start melting down under load
•	14:55 docbrown receives pager storm, ManyHttp500s from all clusters
•	14:57 All traffic to Shakespeare search is failing: see https://monitor
•	14:58 docbrown starts investigating, finds backend crash rate very high
•	15:01 INCIDENT BEGINS docbrown declares incident #465 due to cascading failure, 



