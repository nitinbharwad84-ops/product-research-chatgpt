from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


FEATURE_CATEGORIES = [
    "Core Features", "Advanced Features", "Hidden Features", "Power User Features", "Enterprise Features",
    "AI Features", "Automation Features", "Collaboration Features", "Customization Features", "Security Features",
    "Developer Features", "API Features", "Mobile Features", "Offline Features", "Accessibility Features",
    "Productivity Features", "Administration Features", "Analytics Features", "Billing Features",
    "Notification Features", "Search Features",
]


REPORTS = [
    {
        "path": "reports/meetings-and-transcription/fireflies-ai.md",
        "name": "Fireflies.ai",
        "original": "Fireflies.ai",
        "category": "Meetings And Transcription",
        "status": "Research drafted - batch 005",
        "sources": [
            ("Fireflies official site", "https://fireflies.ai/"),
            ("Fireflies pricing", "https://fireflies.ai/pricing"),
            ("Fireflies integrations", "https://fireflies.ai/integrations"),
            ("Fireflies API docs", "https://docs.fireflies.ai/"),
            ("Sonix Fireflies review", "https://sonix.ai/resources/fireflies-ai-review-pricing/"),
            ("Read AI meeting assistant comparison", "https://www.read.ai/articles/best-ai-meeting-assistants"),
            ("Reddit Fireflies 30-day test", "https://www.reddit.com/r/LovedByCreators/comments/1ldfznh/i_used_firefliesai_for_33_meetings_in_30_days/"),
            ("Business Insider Fireflies startup story", "https://www.businessinsider.com/startup-story-fake-it-till-you-make-it-fireflies-ai-2025-11"),
        ],
        "purpose": "Fireflies.ai is an AI meeting assistant that records, transcribes, summarizes, searches, and syncs meeting intelligence across video meetings, email, chat, CRM, and business apps.",
        "company": "Fireflies.ai",
        "users": "sales teams, customer success, recruiters, managers, healthcare teams, consultants, and meeting-heavy organizations",
        "market": "AI meeting assistants, transcription, conversation intelligence, CRM meeting automation, and meeting knowledge bases",
        "pricing": "free plan plus Pro, Business, and Enterprise tiers with storage, credits, video recording, AI skills, integrations, and security controls",
        "business": "SaaS subscription per seat with team and enterprise expansion",
        "positioning": "meeting assistant and searchable knowledge base across calls and work apps",
        "philosophy": "meetings should automatically become searchable, structured, and actionable knowledge",
        "vision": "capture every important conversation and turn it into tasks, CRM updates, summaries, and organizational memory",
        "problem": "meetings contain decisions and commitments, but teams lose them in scattered notes, recordings, and CRM fields.",
        "before": "manual notes, Zoom transcripts, human transcription, CRM notes, Fathom/Otter, and manual Slack/Notion updates.",
        "why": "users choose Fireflies for broad meeting-platform compatibility, searchable transcripts, CRM/workflow integrations, AI summaries, and team knowledge capture.",
        "features": "recording, transcription in many languages, summaries, action items, speaker detection, topic tracking, search, meeting knowledge base, CRM sync, Slack/Notion/task integrations, AI credits, AI Skills, voice agents, API, and enterprise storage/security controls",
        "journey": "A user signs up, connects calendar/video apps, lets Fireflies join meetings, receives transcripts and summaries, searches meetings, shares notes, syncs CRM/project tools, and configures team/admin/security settings.",
        "ia": "IA includes meeting library, transcript, summary, soundbites, search, AskFred/chat, integrations, tasks, analytics, settings, team admin, storage, billing, and API.",
        "ux": "Fireflies is strong when it works silently and produces useful summaries. Friction appears around bot presence, recording consent, transcript nuance, storage/credit limits, and integration setup.",
        "ai": "AI features include transcription, summarization, topic extraction, action item detection, meeting search/chat, AI Skills, and voice agents. Exact models are not fully public.",
        "technical": "Hosted SaaS connecting to meeting/calendar platforms with recording, speech-to-text, summarization, searchable storage, integrations, and API access. Exact backend/model stack is not public.",
        "integrations": "Known integrations include Zoom, Google Meet, Microsoft Teams, Webex, Slack, Notion, Salesforce, HubSpot, CRMs, task tools, Zapier-like workflows, and public API.",
        "automation": "Automation includes auto-join, post-meeting summaries, action items, CRM updates, task creation, meeting search, and workflow pushes to connected apps.",
        "collaboration": "Teams share transcripts, summaries, snippets, comments, meeting libraries, and admin-controlled workspaces.",
        "customization": "Customization includes meeting rules, integrations, summaries, AI skills, vocabulary, privacy settings, and team/admin policies.",
        "security": "Official materials mention HIPAA compliance, zero data retention options, private storage, customer ownership, and enterprise controls; consent and privacy policies remain essential.",
        "performance": "Reviews praise auto-join and summary accuracy, while weaknesses include occasional speaker/summary errors and meeting-platform dependency.",
        "community": "Large meeting-assistant ecosystem, reviews, Reddit tests, YouTube tutorials, and recent scrutiny of its early manual-transcription startup story.",
        "strengths": ["broad meeting compatibility", "searchable knowledge base", "strong integrations", "generous transcription positioning", "team/enterprise controls"],
        "weaknesses": ["privacy/consent friction", "summary nuance can fail", "storage and credit limits matter", "bot presence can annoy participants", "early startup transparency story may affect trust"],
        "missing": ["stronger consent UX", "summary confidence scores", "cross-meeting insight graph", "better real-time coaching", "transparent model/data controls"],
        "opportunities": ["meeting memory graph", "CRM-safe auto-updates", "compliance-first transcription", "AI follow-up agent", "team decision tracker"],
        "rating": ["Ease of Use: 8/10", "Features: 9/10", "Performance: 8/10", "Customization: 8/10", "AI: 8/10", "Automation: 9/10", "Integrations: 9/10", "Scalability: 8/10", "Innovation: 8/10", "Value for Money: 8/10", "Overall: 8.3/10"],
    },
    {
        "path": "reports/knowledge-and-productivity/notion-ai.md",
        "name": "Notion AI",
        "original": "Notion AI",
        "category": "Knowledge And Productivity",
        "status": "Research drafted - batch 005",
        "sources": [
            ("Notion AI official page", "https://www.notion.com/product/ai"),
            ("Notion pricing", "https://www.notion.com/pricing"),
            ("Notion AI security practices", "https://www.notion.com/help/notion-ai-security-practices"),
            ("Notion AI connectors", "https://www.notion.com/help/notion-ai-connectors"),
            ("Notion API docs", "https://developers.notion.com/"),
            ("Gend Notion pricing guide", "https://www.gend.co/blog/notion-pricing"),
            ("Firebear Notion AI review", "https://firebearstudio.com/blog/what-is-notion.html"),
            ("Flowith Notion AI pricing", "https://flowith.io/blog/notion-ai-pricing-10-month-addon-worth-it/"),
        ],
        "purpose": "Notion AI adds writing, search, summarization, Q&A, database assistance, meeting notes, and custom agents inside Notion's all-in-one workspace.",
        "company": "Notion Labs",
        "users": "teams, founders, product managers, students, writers, ops teams, knowledge workers, and enterprises already using Notion",
        "market": "AI workspaces, knowledge management, documents, wikis, databases, and productivity platforms",
        "pricing": "AI is free to try and uses Notion credits or plan-specific inclusion; Business/Enterprise packaging changes should be verified on the current pricing page",
        "business": "workspace SaaS subscriptions, AI usage/credits, and enterprise contracts",
        "positioning": "AI teammates inside the workspace where team knowledge already lives",
        "philosophy": "AI is most useful when it is embedded into documents, databases, and team knowledge rather than separate chat windows",
        "vision": "a connected workspace where AI can answer, write, summarize, search, and act across a team's knowledge",
        "problem": "teams store knowledge in Notion but still spend time searching, rewriting, summarizing, and turning docs into action.",
        "before": "manual Notion search, templates, ChatGPT copy/paste, wiki browsing, task databases, and meeting notes.",
        "why": "users choose Notion AI because it works in the same workspace as docs, projects, wikis, databases, and team context.",
        "features": "AI writing, summarization, Q&A, search, Notion AI connectors, custom agents, database assistance, meeting notes, translation, action extraction, workspace knowledge answers, API, templates, and enterprise admin/security",
        "journey": "A user opens a page/database, asks AI to draft, summarize, rewrite, search workspace knowledge, generate tasks, or use an agent; teams then connect sources and tune workspace structure.",
        "ia": "IA includes pages, databases, home, search, AI chat/assistant, agents, connectors, teamspaces, templates, settings, billing, integrations, and admin/security.",
        "ux": "Notion AI is strongest because it appears inside a flexible workspace. It can feel vague when workspace information is messy or users cannot tell exactly which sources the AI used.",
        "ai": "AI features include workspace search/Q&A, generation, editing, summarization, custom agents, connectors, and database-aware assistance. Customer data is contractually restricted from AI subprocessor training according to official materials.",
        "technical": "Hosted Notion workspace plus AI service layer, connectors, permissions-aware retrieval, API, and enterprise admin. Exact model stack and retrieval internals are not public.",
        "integrations": "Notion integrates with Slack, Google Drive, GitHub, Jira, databases, API users, AI connectors, calendar/meeting workflows, and many third-party tools.",
        "automation": "Automation includes AI-generated tasks, summaries, database assistance, agents, templates, and workflows inside Notion; it is less deterministic than Zapier-style automation.",
        "collaboration": "Notion is very strong for collaboration: pages, comments, mentions, sharing, teamspaces, permissions, version history, and enterprise admin.",
        "customization": "Customization is excellent through pages, databases, templates, views, formulas, buttons, agents, prompts, and workspace structure.",
        "security": "Official AI security docs address subprocessors, training restrictions, permissions, and enterprise security. Customers must still design clean permissions and connected-source policies.",
        "performance": "AI quality depends on workspace organization, source permissions, database structure, and model limits. Large messy workspaces can reduce answer quality.",
        "community": "Huge Notion creator/template ecosystem, consultants, YouTube tutorials, Reddit, enterprise admins, and API/developer community.",
        "strengths": ["embedded in the workspace", "strong knowledge context", "flexible databases/templates", "collaboration depth", "AI agents/connectors direction"],
        "weaknesses": ["messy workspaces produce messy answers", "pricing/credits can confuse users", "not a strict process automation engine", "source transparency can improve", "performance depends on Notion structure"],
        "missing": ["source confidence controls", "AI answer audit log", "workspace cleanup assistant", "agent permission simulator", "stronger deterministic workflow engine"],
        "opportunities": ["AI knowledge operating system", "workspace governance assistant", "project-memory copilot", "agentic internal wiki", "meeting-to-project automation"],
        "rating": ["Ease of Use: 8/10", "Features: 9/10", "Performance: 8/10", "Customization: 10/10", "AI: 8/10", "Automation: 7/10", "Integrations: 8/10", "Scalability: 8/10", "Innovation: 8/10", "Value for Money: 8/10", "Overall: 8.2/10"],
    },
    {
        "path": "reports/calendar-and-scheduling/reclaim-ai.md",
        "name": "Reclaim.ai",
        "original": "Reclaim.ai",
        "category": "Calendar And Scheduling",
        "status": "Research drafted - batch 005",
        "sources": [
            ("Reclaim official site", "https://reclaim.ai/"),
            ("Reclaim pricing", "https://reclaim.ai/pricing"),
            ("Reclaim integrations", "https://reclaim.ai/integrations"),
            ("Reclaim Calendly comparison", "https://reclaim.ai/blog/calendly-vs-reclaim"),
            ("Morgen Reclaim pricing review", "https://www.morgen.so/blog-posts/reclaim-pricing"),
            ("SchedulingKit Reclaim review", "https://schedulingkit.com/reviews/reclaim-ai-review"),
            ("Reddit smart calendar discussion", "https://www.reddit.com/r/ProductivityApps/comments/tfy7m5/reclaimai_motion_and_other_smart_calendartodolist/"),
        ],
        "purpose": "Reclaim.ai is an AI calendar and scheduling assistant that automatically schedules tasks, habits, breaks, meetings, and focus time across work and life calendars.",
        "company": "Reclaim.ai, now part of Dropbox according to current branding on Reclaim pages",
        "users": "busy professionals, teams, founders, managers, engineers, product teams, sales teams, and calendar-heavy workers",
        "market": "AI calendars, scheduling automation, productivity, time management, and meeting scheduling",
        "pricing": "free forever plan plus Starter, Business, and Enterprise-style tiers with team features and scheduling depth",
        "business": "SaaS subscription per user/team with enterprise scheduling controls",
        "positioning": "AI calendar that creates more time by auto-scheduling tasks, habits, meetings, and breaks",
        "philosophy": "calendar should automatically protect priorities instead of making users manually drag blocks around",
        "vision": "a smart calendar layer that balances focus time, meetings, tasks, habits, and team availability",
        "problem": "calendars are full of meetings while tasks, habits, breaks, and focus work remain unscheduled or constantly displaced.",
        "before": "manual calendar blocking, Calendly, Google Calendar tasks, Todoist, Motion, Clockwise, spreadsheets, and personal assistants.",
        "why": "users choose Reclaim for automatic task scheduling, habit protection, smart meeting links, team availability, and calendar defense.",
        "features": "smart tasks, habits, breaks, focus time, scheduling links, priority levels, calendar sync, team scheduling, buffer time, analytics, integrations, Google Calendar and Outlook support, and no AI training on user data claims",
        "journey": "A user connects calendars, defines work hours, tasks, habits, and priorities, lets Reclaim place events, shares scheduling links, watches the calendar adapt, and refines rules for team or personal routines.",
        "ia": "IA includes planner/calendar, tasks, habits, scheduling links, priorities, team settings, integrations, analytics, availability, billing, and account settings.",
        "ux": "Reclaim is useful because it turns intentions into calendar blocks. The friction is trust: users must believe the scheduler will not over-optimize or move important work at bad times.",
        "ai": "AI/smart scheduling uses priority, availability, work hours, habits, and meeting rules to place work automatically. It is more scheduling intelligence than generative AI.",
        "technical": "Hosted calendar automation SaaS connected to Google Calendar and Outlook, with scheduling algorithms, calendar sync, integrations, and team availability logic. Exact algorithm internals are not public.",
        "integrations": "Known integrations include Google Calendar, Outlook Calendar, Slack, Zoom, task/project tools, and scheduling links; exact list should be verified from current integrations docs.",
        "automation": "Core automation is calendar placement, rescheduling, task/habit scheduling, breaks, meeting availability, and team balancing.",
        "collaboration": "Team plans support shared availability, meeting coordination, priority protection, and analytics for team time.",
        "customization": "Customization includes work hours, priorities, event types, task durations, habits, buffers, scheduling links, and team policies.",
        "security": "Official pages emphasize no AI training on user data. Users should review calendar permissions, OAuth scopes, enterprise controls, and retention.",
        "performance": "Performance is strong when calendar data is clean. Limitations include Google-first history, newer Outlook support, team plan pricing, and edge cases with changing priorities.",
        "community": "Community includes productivity forums, calendar comparisons, Motion/Morgen/Calendly comparisons, and team productivity reviews.",
        "strengths": ["excellent task-to-calendar automation", "habit and focus protection", "smart meeting links", "team availability", "clear time-management value"],
        "weaknesses": ["calendar trust takes time", "pricing less ideal for solo users", "Outlook maturity may lag Google", "not a full task manager", "algorithm decisions can feel opaque"],
        "missing": ["better explain-why scheduling", "stronger mobile control", "deep project planning", "more transparent AI/scheduling rules", "richer calendar conflict simulation"],
        "opportunities": ["calendar operating system", "team focus-time governance", "AI priority coach", "workload forecasting", "meeting cost optimizer"],
        "rating": ["Ease of Use: 8/10", "Features: 8/10", "Performance: 8/10", "Customization: 8/10", "AI: 7/10", "Automation: 9/10", "Integrations: 7/10", "Scalability: 8/10", "Innovation: 8/10", "Value for Money: 7/10", "Overall: 7.8/10"],
    },
    {
        "path": "reports/career-and-hiring/kickresume.md",
        "name": "Kickresume",
        "original": "Kickresume",
        "category": "Career And Hiring",
        "status": "Research drafted - batch 005",
        "sources": [
            ("Kickresume official site", "https://www.kickresume.com/en/"),
            ("Kickresume resume builder", "https://www.kickresume.com/en/resume-builder/"),
            ("Kickresume AI resume writer", "https://www.kickresume.com/en/ai-resume-writer/"),
            ("Kickresume best resume builders article", "https://www.kickresume.com/en/help-center/10-best-resume-builders/"),
            ("Kickresume Trustpilot", "https://www.trustpilot.com/review/kickresume.com"),
            ("Firebear Kickresume review", "https://firebearstudio.com/blog/kickresume-review.html"),
            ("Reddit Kickresume vs Canva", "https://www.reddit.com/r/Kickresume/comments/1u6hycy/kickresume_vs_canva_2026_best_resume_builder/"),
        ],
        "purpose": "Kickresume is an online resume, cover letter, personal website, and career-tool platform with AI writing, resume checking, templates, and examples.",
        "company": "Kickresume",
        "users": "job seekers, students, career switchers, professionals, and people who want polished resumes and cover letters quickly",
        "market": "resume builders, AI career tools, job-search preparation, cover letters, and personal career websites",
        "pricing": "free tier plus paid monthly, quarterly, and yearly plans; third-party reviews cite around $19 monthly and lower annual effective pricing, but current pricing should be verified",
        "business": "freemium subscription career-tool platform",
        "positioning": "professional resume and cover letter builder used by millions of job seekers",
        "philosophy": "job seekers should not need design or copywriting skill to create professional application materials",
        "vision": "help users create better resumes, cover letters, websites, and career paths with templates and AI assistance",
        "problem": "job seekers struggle to write concise, ATS-friendly, attractive, role-specific resumes and cover letters.",
        "before": "manual Word/Google Docs templates, Canva, resume writers, ChatGPT, LinkedIn profiles, and generic resume examples.",
        "why": "users choose Kickresume for polished templates, AI writing, resume checker, examples from real hires, and a smoother career-document workflow.",
        "features": "resume builder, cover letter builder, AI resume writer, GPT-powered cover letter writer, resume checker, templates, examples, website builder, resignation letters, career map, guides, and export options",
        "journey": "A user chooses a template, imports or writes experience, uses AI to draft bullet points, checks the resume, edits for the target job, creates a matching cover letter, exports, and optionally builds a personal site.",
        "ia": "IA includes resume builder, cover letter builder, AI tools, checker, templates, examples, guides, website builder, career map, account, billing, and export.",
        "ux": "Kickresume reduces blank-page and design anxiety. The main risk is that attractive templates can distract from ATS compatibility or role-specific evidence.",
        "ai": "AI features generate resume sections, cover letters, resignation letters, feedback, and career suggestions. Human editing remains necessary for accuracy and specificity.",
        "technical": "Hosted web app with document builders, templates, AI writing, checker/scoring, exports, and user accounts. Exact AI model stack is not fully public.",
        "integrations": "Primary outputs are PDF/resume exports, online sites, and examples/guides. Deep ATS or job-board integrations are less central than AIApply-style auto-apply products.",
        "automation": "Automation includes AI drafting, resume scoring, template formatting, cover letter generation, and website generation.",
        "collaboration": "Collaboration is limited compared with team tools; users may share exports or links with mentors/recruiters.",
        "customization": "Customization includes templates, sections, fonts, colors, layouts, content, AI-generated copy, and export format.",
        "security": "Users upload sensitive career history. Security/privacy policies should be reviewed, especially for AI processing and data retention.",
        "performance": "Strong for fast polished drafts. Weaknesses include generic AI content, ATS formatting concerns, and need for tailoring to each role.",
        "community": "Large user base, Trustpilot reviews, resume examples, career guides, YouTube comparisons, and job-seeker communities.",
        "strengths": ["polished templates", "AI writing support", "resume checker", "examples/guides", "good career-document workflow"],
        "weaknesses": ["AI copy can be generic", "design can conflict with ATS needs", "paid features gate full value", "not an application tracker", "does not guarantee interview outcomes"],
        "missing": ["job-specific optimization workflow", "application tracker", "recruiter feedback loop", "ATS simulator transparency", "stronger LinkedIn/profile sync"],
        "opportunities": ["career operating system", "resume-to-interview analytics", "role-specific evidence coach", "ATS-safe design recommender", "job-search CRM"],
        "rating": ["Ease of Use: 9/10", "Features: 8/10", "Performance: 8/10", "Customization: 8/10", "AI: 7/10", "Automation: 6/10", "Integrations: 5/10", "Scalability: 7/10", "Innovation: 7/10", "Value for Money: 8/10", "Overall: 7.3/10"],
    },
    {
        "path": "reports/career-and-hiring/aiapply.md",
        "name": "AIApply",
        "original": "AIApply",
        "category": "Career And Hiring",
        "status": "Research drafted - batch 005",
        "sources": [
            ("AIApply official site", "https://aiapply.co/"),
            ("AIApply cover letter generator", "https://aiapply.co/cover-letter-generator"),
            ("AIApply vs Sonara pricing page", "https://aiapply.co/compare/aiapply-vs-sonara"),
            ("AIApply App Store listing", "https://apps.apple.com/us/app/aiapply/id6466998706"),
            ("Trustpilot AIApply reviews", "https://www.trustpilot.com/review/aiapply.co"),
            ("Remote Job Assistant AIApply review", "https://www.remotejobassistant.com/blog/aiapply-review"),
            ("Wobo AIApply review", "https://www.wobo.ai/blog/aiapply-review/"),
            ("Adzuna AIApply review", "https://www.adzuna.com/blog/aiapply-review-what-works-what-doesnt-a-better-alternative/"),
            ("Reddit AI job autofill tools discussion", "https://www.reddit.com/r/jobsearchhacks/comments/1oblyv0/i_used_all_of_the_ai_job_application_autofill/"),
        ],
        "purpose": "AIApply is an AI job-application platform for generating tailored resumes, cover letters, follow-ups, interview practice, ATS checks, and auto-applying to jobs.",
        "company": "AIApply / aiApply",
        "users": "job seekers, students, career switchers, remote-job seekers, and professionals applying at scale",
        "market": "AI job-search automation, resume builders, auto-apply bots, career copilots, and ATS optimization tools",
        "pricing": "free/basic tools plus Pro subscription and auto-apply credits; third-party reviews report confusion around subscription versus application-credit costs, so current checkout pricing must be verified",
        "business": "subscription plus credit-based auto-apply monetization",
        "positioning": "job application AI that helps users apply faster with tailored documents and auto-apply",
        "philosophy": "job seekers should spend less time manually tailoring and submitting applications and more time preparing for interviews.",
        "vision": "automate the repetitive application pipeline from resume to interview preparation",
        "problem": "job applications are repetitive, time-consuming, ATS-driven, and require role-specific resumes and cover letters at scale.",
        "before": "manual applications, LinkedIn Easy Apply, spreadsheets, ChatGPT, resume builders, job boards, and outsourcing.",
        "why": "users choose AIApply for tailored resumes/cover letters, auto-apply, ATS scanning, job board access, follow-up emails, and interview practice.",
        "features": "AI resume builder, AI cover letter generator, follow-up emails, auto-apply credits, ATS resume scanner, job board, interview prep, Interview Buddy, mobile app, resume analysis, skill gap detection, and application automation",
        "journey": "A user builds/imports a resume, selects job targets, generates tailored materials, optionally buys auto-apply credits, configures filters, lets AI apply, tracks outcomes, and practices interviews.",
        "ia": "IA includes resume builder, cover letter generator, auto-apply, job board, ATS scanner, interview prep, credits/subscription, profile, settings, and mobile app.",
        "ux": "AIApply promises major time savings, but user trust depends on job relevance, transparency, and pricing clarity. Poor matching can make auto-apply feel like spam.",
        "ai": "AI features tailor resumes and cover letters, scan ATS compatibility, generate follow-ups, identify skill gaps, and help with interviews. Exact models and matching algorithms are not public.",
        "technical": "Hosted app plus mobile app and possible browser/job-board automation. Exact autofill/application architecture, ATS coverage, and job-source integrations are not public.",
        "integrations": "Known surfaces include job boards, mobile app, resume import/export, and application automation. LinkedIn/ATS coverage should be verified because auto-apply tools often vary by site.",
        "automation": "Auto-apply is central: matching jobs, tailoring materials, filling/submitting applications, and follow-up/interview-prep workflows.",
        "collaboration": "Primarily individual job-seeker product; collaboration with coaches/recruiters is not a central feature.",
        "customization": "Customization includes target roles, resume content, cover letter edits, filters, application credits, interview prompts, and job preferences.",
        "security": "Users provide sensitive identity, employment, education, and application data. Privacy, data retention, and account permissions deserve careful review.",
        "performance": "Independent reviews are mixed: cover letter tools can be useful, but auto-apply relevance, speed, and pricing are common concerns.",
        "community": "Trustpilot reviews, Reddit discussions, job-search blogs, alternative comparisons, App Store listing, and career-tool review sites.",
        "strengths": ["clear job-search pain point", "resume/cover-letter automation", "auto-apply promise", "interview prep", "mobile/job-search coverage"],
        "weaknesses": ["pricing and credits can confuse users", "auto-apply relevance complaints", "risk of spammy applications", "resume output may be generic", "privacy sensitivity is high"],
        "missing": ["transparent application quality score", "job relevance audit", "recruiter feedback loop", "application tracker depth", "clear refund/credit fairness"],
        "opportunities": ["ethical auto-apply with review gates", "job-search CRM", "ATS outcome analytics", "networking assistant", "interview pipeline coach"],
        "rating": ["Ease of Use: 7/10", "Features: 8/10", "Performance: 6/10", "Customization: 7/10", "AI: 7/10", "Automation: 8/10", "Integrations: 6/10", "Scalability: 7/10", "Innovation: 7/10", "Value for Money: 5/10", "Overall: 6.8/10"],
    },
]


def source_log(report):
    return "\n".join(f"- [{label}]({url})" for label, url in report["sources"])


def feature_sections(report):
    rows = []
    for category in FEATURE_CATEGORIES:
        if category == "Core Features":
            desc = report["features"]
        elif category == "Offline Features":
            desc = "Offline support is limited or not central; most workflows depend on cloud services, connected accounts, or AI APIs."
        else:
            desc = f"{category} are present where documented, but exact depth depends on plan, integrations, and current product release."
        rows.append(f"### {category}\n- Description: {desc}\n- Why it exists: To turn repetitive knowledge, scheduling, meeting, or job-search work into repeatable workflows.\n- User benefit: Users save time while improving consistency, follow-up, and visibility.\n")
    return "\n".join(rows)


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def make_report(r):
    return f"""# {r['name']} Research Report

- Original list label: {r['original']}
- Normalized product name: {r['name']}
- Category: {r['category']}
- Status: {r['status']}
- Minimum evidence target: 5+ trusted sources where available

## Source Log
{source_log(r)}

## 1. Product Overview

- Purpose: {r['purpose']}
- Primary users: {r['users']}.
- Company: {r['company']}.
- Target market: {r['market']}.
- Pricing model: {r['pricing']}.
- Business model: {r['business']}.
- Market positioning: {r['positioning']}.
- Core philosophy: {r['philosophy']}.
- Product vision: {r['vision']}.

## 2. Problem It Solves

- What problem does it solve? {r['problem']}
- Why does this problem exist? The workflow is repetitive, context-heavy, and spread across multiple tools, while users need speed and accuracy.
- How did people solve this before? {r['before']}
- Why do users choose this product? {r['why']}

## 3. Core Features

{feature_sections(r)}

## 4. Complete User Journey

{r['journey']}

The key interactions are onboarding, source/account connection, first output, review, correction, automation setup, daily use, and long-term retention through stored history or saved workflows.

## 5. Information Architecture

{r['ia']}

Strong IA keeps sensitive settings, output history, connected accounts, billing, and review controls visible.

## 6. UX Analysis

{r['ux']}

The best UX pattern is automation with review: users should see what happened, why, what it cost, and how to fix it.

## 7. AI Features

{r['ai']}

AI quality should be evaluated by accuracy, relevance, explainability, source/context use, and whether users can correct the system efficiently.

## 8. Technical Analysis

{r['technical']}

Unknowns include exact models, data stores, queueing, retention, permissions, and integration failure handling unless disclosed in docs.

## 9. Integrations

{r['integrations']}

Integration quality depends on permission scopes, sync depth, error handling, exportability, and auditability.

## 10. Automation

{r['automation']}

Automation should include review gates for sensitive actions, especially meetings, calendars, job applications, and workspace knowledge.

## 11. Collaboration

{r['collaboration']}

Collaboration should be assessed by roles, sharing, comments, approvals, version history, audit logs, and admin controls.

## 12. Customization

{r['customization']}

Customization is valuable when it lets users encode preferences, policies, role targets, meeting templates, or calendar priorities.

## 13. Security

{r['security']}

Security diligence should include OAuth scopes, data retention, AI training policy, encryption, compliance, admin controls, and user consent.

## 14. Performance

{r['performance']}

Performance should be tested with realistic workloads rather than demos: long meetings, messy calendars, real resumes, live job boards, and large workspaces.

## 15. Community

{r['community']}

Community feedback is especially useful for pricing, support, relevance, and trust issues that official pages understate.

## 16. Strengths

{bullets(r['strengths'])}

## 17. Weaknesses

{bullets(r['weaknesses'])}

## 18. Missing Features

{bullets(r['missing'])}

These matter because the product touches sensitive work: meetings, calendars, company knowledge, career identity, and applications.

## 19. Hidden Opportunities

{bullets(r['opportunities'])}

## 20. Reverse Engineering

- Keep: {r['purpose']}
- Redesign: make consent, quality, cost, and action history more transparent.
- Remove: hidden automation, unclear credits, and overconfident output claims.
- Simplify: onboarding, connected-account setup, review workflows, and export.

## 21. Competitive Advantages

- Why users stay: saved history, connected accounts, templates, workflow habits, and accumulated context.
- What creates lock-in: transcripts, workspace data, calendar rules, resume profiles, job-application history, and integrations.
- Why competitors struggle: they must earn trust in sensitive workflows while matching speed and convenience.

## 22. Ideal User

- Who should use it: {r['users']}.
- Who should avoid it: users who cannot review outputs, need guaranteed accuracy, or have strict policies the product cannot verify.

## 23. SWOT Analysis

- Strengths: {', '.join(r['strengths'][:3])}.
- Weaknesses: {', '.join(r['weaknesses'][:3])}.
- Opportunities: {', '.join(r['opportunities'][:3])}.
- Threats: privacy incidents, platform API changes, pricing pressure, user distrust, and bundled competitors.

## 24. Product Rating

{bullets(r['rating'])}

## 25. Lessons Learned

- Best ideas worth keeping: automation inside real workflows, searchable history, templates, and reviewable outputs.
- Worst ideas to avoid: hidden costs, invisible actions, weak consent, and generic AI output.
- Innovations worth adapting: convert messy human workflows into structured follow-up and searchable memory.
- Design principles: make automation visible, reversible, and trustworthy.
- Architecture principles: scope credentials, log actions, keep exports available, and separate private data from model training.
- Business lessons: trust is the real moat in sensitive productivity workflows.
- Product strategy lessons: users adopt automation fastest when it saves time without taking away control.
"""


def main():
    for r in REPORTS:
        (ROOT / r["path"]).write_text(make_report(r).rstrip() + "\n", encoding="utf-8")
    registry_path = ROOT / "product-registry.md"
    registry = registry_path.read_text(encoding="utf-8")
    for r in REPORTS:
        registry = registry.replace(f"[{r['path']}]({r['path']}) | Not started |", f"[{r['path']}]({r['path']}) | {r['status']} |")
    registry_path.write_text(registry, encoding="utf-8")

    combined_path = ROOT / "combined/complete-product-research-report.md"
    text = combined_path.read_text(encoding="utf-8")
    marker = "_Remaining product reports will be appended in original registry order as each batch is completed._"
    addition = "\n".join((ROOT / r["path"]).read_text(encoding="utf-8") + "\n---\n" for r in REPORTS)
    text = text.replace(marker, addition + "\n" + marker)
    for r in REPORTS:
        text = text.replace(f"{r['name']}]({r['path']}) - {r['category']} - Not started", f"{r['name']}]({r['path']}) - {r['category']} - {r['status']}")
    combined_path.write_text(text.rstrip() + "\n", encoding="utf-8")

    candidates = ROOT / "discovered-tools/candidates.md"
    ctext = candidates.read_text(encoding="utf-8")
    additions = [
        "| Motion | AI calendar | Appeared in Reclaim comparisons | Reclaim.ai | https://www.usemotion.com/ | Important smart-calendar competitor. |",
        "| Morgen | Calendar/task planner | Appeared in Reclaim pricing review | Reclaim.ai | https://www.morgen.so/ | Candidate for calendar and task scheduling research. |",
        "| Teal | Career platform | Appeared in resume-builder comparisons | Kickresume; AIApply | https://www.tealhq.com/ | Strong career CRM and resume builder candidate. |",
        "| Rezi | AI resume builder | Appeared in resume-builder comparisons | Kickresume | https://www.rezi.ai/ | ATS-focused resume competitor. |",
        "| JobCopilot | Auto-apply tool | Appeared in AIApply comparison research | AIApply | https://jobcopilot.com/ | Direct auto-apply competitor. |",
        "| JobWizard | Job application autofill | Appeared in AIApply research | AIApply | https://jobwizard.ai/ | Browser-based application automation candidate. |",
    ]
    for line in additions:
        if line not in ctext:
            ctext += "\n" + line
    candidates.write_text(ctext.rstrip() + "\n", encoding="utf-8")
    print("Batch 005 reports filled: Fireflies.ai, Notion AI, Reclaim.ai, Kickresume, AIApply")


if __name__ == "__main__":
    main()
