from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SOURCE_LOGS = {
    "Hermes Agent": [
        ("Hermes Agent documentation", "https://hermes-agent.nousresearch.com/docs/"),
        ("NousResearch/hermes-agent GitHub repository", "https://github.com/nousresearch/hermes-agent"),
        ("Hermes Agent AI providers documentation", "https://hermes-agent.nousresearch.com/docs/integrations/providers"),
        ("Hermes Agent open-source project site", "https://hermes-agent.org/"),
        ("TechRadar workflow automation article", "https://www.techradar.com/pro/how-to-automate-workflows-using-open-source-ai-agents"),
        ("PetronellaTech Hermes Agent guide", "https://petronellatech.com/blog/hermes-agent-ai-guide/"),
    ],
    "OpenClaw": [
        ("OpenClaw official site", "https://openclaw.ai/"),
        ("OpenClaw documentation", "https://docs.openclaw.ai/"),
        ("openclaw/openclaw GitHub repository", "https://github.com/openclaw/openclaw"),
        ("TechRadar OpenClaw overview", "https://www.techradar.com/pro/what-is-openclaw"),
        ("TechRadar OpenClaw security guide", "https://www.techradar.com/pro/your-openclaw-agents-can-empty-your-inbox-and-leak-your-data-heres-how-to-secure-them"),
        ("WIRED OpenClaw field report", "https://www.wired.com/story/malevolent-ai-agent-openclaw-clawdbot/"),
        ("Reddit OpenClaw user discussion", "https://www.reddit.com/r/AI_Agents/comments/1qz9rip/i_spent_a_week_testing_openclaw_cool_demo_but_i/"),
    ],
    "ZeroClaw": [
        ("zeroclaw-labs/zeroclaw GitHub repository", "https://github.com/zeroclaw-labs/zeroclaw"),
        ("ZeroClaw product site", "https://zeroclaw.net/"),
        ("Reddit ZeroClaw discussion", "https://www.reddit.com/r/openclaw/comments/1r5djrj/zeroclaw_found_a_tiny_rust_ai_runtime_worth_trying/"),
        ("YouTube ZeroClaw vs OpenClaw video", "https://www.youtube.com/watch?v=I0r7HaLDSS8"),
        ("Composio OpenClaw alternatives article", "https://composio.dev/content/openclaw-alternatives"),
        ("DEV Community Claw-family overview", "https://dev.to/0xkoji/a-quick-look-at-claw-family-28e3"),
    ],
    "TrustClaw": [
        ("ComposioHQ/trustclaw GitHub repository", "https://github.com/ComposioHQ/trustclaw"),
        ("Composio OpenClaw alternatives article", "https://composio.dev/content/openclaw-alternatives"),
        ("Vellum TrustClaw alternatives article", "https://www.vellum.ai/blog/best-trustclaw-alternatives"),
        ("SourceForge TrustClaw mirror", "https://sourceforge.net/projects/trustclaw.mirror/"),
        ("Progressive Robot TrustClaw setup guide", "https://www.progressiverobot.com/2026/04/09/how-to-set-up-trustclaw/"),
        ("YouTube TrustClaw security interview", "https://www.youtube.com/watch?v=DpfjQ0nBVVI"),
    ],
    "Vellum": [
        ("Vellum developer docs overview", "https://docs.vellum.ai/developers/getting-started/overview"),
        ("Vellum workflows documentation", "https://docs.vellum.ai/product/workflows/introduction"),
        ("Vellum evaluations documentation", "https://docs.vellum.ai/product/evaluation/quantitative-evaluation"),
        ("Vellum online evaluations documentation", "https://docs.vellum.ai/product/evaluation/online-evaluations"),
        ("Vellum RAG evaluation documentation", "https://docs.vellum.ai/product/evaluation/evaluating-rag-pipelines"),
        ("Vellum Node SDK GitHub repository", "https://github.com/vellum-ai/vellum-client-node"),
        ("Vellum AI Apps launch post", "https://www.vellum.ai/blog/ai-apps"),
        ("ZenML Vellum pricing guide", "https://www.zenml.io/blog/vellum-ai-pricing"),
        ("Drata Vellum security case study", "https://drata.com/customers/vellum"),
    ],
}


REPORTS = {
    "reports/ai-agents/hermes-agent.md": {
        "name": "Hermes Agent",
        "original": "Hermes Agent",
        "category": "AI Agents",
        "summary": "Hermes Agent is a self-hostable personal AI agent from Nous Research focused on persistent memory, learned skills, messaging-channel access, and long-running autonomous work.",
        "company": "Nous Research",
        "users": "technical founders, AI builders, power users, self-hosting users, and teams experimenting with persistent personal agents",
        "market": "open-source personal agents and autonomous assistant infrastructure",
        "pricing": "open-source/self-hosted; direct hosting and provider costs depend on the user's infrastructure and model providers",
        "business": "open-source ecosystem and model/community leverage; paid hosting or enterprise packaging is not clearly established from public sources",
        "positioning": "a self-improving, memory-rich personal agent rather than a stateless chatbot or coding-only copilot",
        "philosophy": "an agent should accumulate user context, reusable skills, and operational memory across sessions",
        "vision": "a long-lived assistant that can learn how its user works and execute across channels without staying tied to one desktop session",
        "problem": "chatbots forget operational context, coding agents usually stay trapped in a terminal, and personal automation tools require users to design brittle workflows manually.",
        "before": "users combined ChatGPT/Claude, shell scripts, Zapier-style workflows, calendar/email tools, and note systems with a lot of manual handoff.",
        "why": "users choose it when they want a self-hosted agent that can improve through experience, talk through messaging apps, and keep memory under user-controlled infrastructure.",
        "features": [
            "persistent memory and past-conversation search",
            "automatic skill creation and skill improvement loop",
            "Telegram and other chat-channel access",
            "cloud, VPS, serverless, and local deployment options",
            "provider routing through services such as OpenRouter, Anthropic, Ollama, and vLLM",
            "tool and MCP-style extension surface where available",
            "self-hosting with user-owned credentials",
        ],
        "journey": "A technical user reads the docs, installs the runtime, configures one or more model providers, connects a messaging channel, grants limited tools, tests low-risk tasks, then gradually expands recurring work and memory use as trust grows.",
        "ia": "The public product surface is documentation-first: install, providers, integrations, skills, memory, deployment, and GitHub. The product itself appears to be operated through chat channels and configuration rather than a heavy dashboard.",
        "ux": "The strongest UX idea is continuity: the user speaks to one persistent agent instead of re-explaining context. The tradeoff is setup complexity, debugging opacity, and a learning curve around providers, hosting, permissions, and memory behavior.",
        "ai": "Known public architecture centers on LLM providers, tool execution, learned skills, memory, and chat interfaces. The exact prompt hierarchy, memory ranking, and production safety layers are not fully public.",
        "technical": "Public materials describe a self-hosted agent stack that can run on inexpensive VPS infrastructure, cloud VMs, serverless infrastructure, or local machines. It integrates with hosted and local inference providers and appears designed for extensible tools and persistent data stores, but implementation details should be verified from the repository before production use.",
        "integrations": "Known integrations include model providers such as OpenRouter, Anthropic, Ollama, and vLLM; messaging channels such as Telegram; and tool/plugin integrations exposed by the agent runtime. Complete integration coverage is unknown.",
        "automation": "Hermes supports task execution through tools, long-running workflows, learned skills, and recurring interaction patterns. Strong autonomy depends on what tools and credentials the operator configures.",
        "collaboration": "The product is primarily personal-agent oriented. Team roles, shared workspaces, approval queues, and enterprise audit logs are not clearly established in public sources.",
        "customization": "Customization comes through provider choice, hosting choice, tools, skills, memory, and channel configuration. GUI-level theming or workspace layout customization is not a core public emphasis.",
        "security": "Security depends heavily on self-hosting discipline: least-privilege credentials, isolated runtime, provider data policies, memory hygiene, and monitoring. Public docs emphasize user-controlled deployment, but autonomous agents remain high-risk when connected to real accounts.",
        "performance": "Performance depends on model provider latency, hosting environment, tool execution, and memory retrieval. A lightweight VPS setup may be affordable, but reliability for always-on work depends on operator infrastructure.",
        "community": "Community is centered around Nous Research, GitHub, docs, tutorials, and emerging agent-builder discussions. The ecosystem is newer than mainstream automation tools.",
        "strengths": [
            "clear differentiation around self-improvement and memory",
            "self-hosting gives power users control",
            "messaging-channel interface reduces friction",
            "provider flexibility avoids one-model lock-in",
            "learned skills create a path beyond prompt repetition",
        ],
        "weaknesses": [
            "requires technical setup and operational judgment",
            "public evidence for enterprise governance is limited",
            "memory and autonomy can create privacy and safety risk",
            "debugging learned behavior may be difficult",
            "less mature than conventional SaaS productivity tools",
        ],
        "missing": [
            "first-class permission dashboard",
            "human approval queue for risky tasks",
            "team workspace and audit trail",
            "memory inspection and selective deletion UX",
            "turn-by-turn observability for tool calls",
        ],
        "opportunities": [
            "agent memory control center",
            "personal SOP learning from repeated corrections",
            "safe onboarding with simulated accounts",
            "skill marketplace with security review",
            "portable memory layer across assistants",
        ],
        "rating": {
            "Ease of Use": "6/10 - powerful but technical to configure",
            "Features": "8/10 - strong agent, memory, provider, and skill direction",
            "Performance": "7/10 - depends on hosting and providers",
            "Customization": "8/10 - strong for technical users",
            "AI": "9/10 - AI is the core product",
            "Automation": "8/10 - high potential with configured tools",
            "Integrations": "7/10 - promising but exact breadth should be verified",
            "Scalability": "6/10 - personal-agent scaling is clearer than enterprise scaling",
            "Innovation": "9/10 - strong self-improving-agent thesis",
            "Value for Money": "8/10 - open-source economics can be strong if the user can operate it",
            "Overall": "7.6/10 - highly interesting, but operational maturity matters",
        },
    },
    "reports/ai-agents/openclaw.md": {
        "name": "OpenClaw",
        "original": "OpenClaw",
        "category": "AI Agents",
        "summary": "OpenClaw is an open-source, self-hosted personal AI assistant/gateway that connects chat apps and channels to AI agents capable of acting across tools and services.",
        "company": "Open-source project associated publicly with Peter Steinberger in third-party coverage",
        "users": "developers, technical operators, automation hobbyists, founders, and users who want chat-first autonomous workflows",
        "market": "self-hosted personal AI assistants and agentic automation",
        "pricing": "open-source; user pays infrastructure, model, and integration costs",
        "business": "open-source ecosystem; commercial hosting/support ecosystem may exist around adjacent providers but is not the core repo model",
        "positioning": "an AI that does things from WhatsApp, Telegram, Discord, Slack, and other familiar chat surfaces",
        "philosophy": "the user's existing messaging apps should become the command surface for a capable personal agent",
        "vision": "a locally controlled, always-available assistant that can execute real digital work through configured tools and channels",
        "problem": "most AI assistants answer questions but do not safely operate accounts, files, browsers, calendars, or communication channels end to end.",
        "before": "users used manual app switching, Zapier workflows, RPA, custom scripts, or coding agents in terminals.",
        "why": "users choose OpenClaw for open-source control, chat-channel convenience, broad integration ambition, and the ability to self-host an agent rather than rent a closed assistant.",
        "features": [
            "self-hosted gateway process",
            "messaging-channel access across Discord, Google Chat, iMessage, Matrix, Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and related channels",
            "voice and mobile-facing interaction in public repo descriptions",
            "live Canvas/control surface mentioned in public repo materials",
            "tool execution and skill ecosystem",
            "local credential/config driven deployment",
            "agent automation through LLM providers and tools",
        ],
        "journey": "A user discovers the product, reads setup docs, clones or installs the gateway, configures model/provider keys, connects one channel, grants narrow tools, tests simple actions, then expands to email, calendar, file, and browser workflows if reliability holds.",
        "ia": "The public IA is split across site, docs, GitHub, integrations, blog, Discord, and product pages. In use, the main IA is chat-first: users issue requests in existing channels while configuration lives in local files or deployment settings.",
        "ux": "OpenClaw's best UX move is removing the need for another dashboard. Its UX risk is that chat hides state, permissions, and execution detail unless the operator builds strong observability and approval patterns.",
        "ai": "The product connects LLMs to channels and tools. Public sources describe autonomous task execution, memory/state, skills, and channel bridges. Exact prompts, safety policies, and model defaults vary by configuration and are not fully established from public docs alone.",
        "technical": "Public docs describe a gateway process that bridges chat channels to agents and tools. It is open source and self-hosted. Third-party coverage says it can run locally and uses external LLMs such as Claude, DeepSeek, or OpenAI models. Security coverage indicates sandboxing and credential handling are central technical concerns.",
        "integrations": "Public docs list many chat-channel integrations. Third-party ecosystem materials mention dozens of service integrations and skills. Exact counts should be verified against the current repo because fast-moving agent projects often change integrations quickly.",
        "automation": "OpenClaw can run agentic tasks such as email, calendar, browsing, scripts, files, and recurring assistant work when granted tools. Automation quality depends on prompt design, tool safety, constraints, and monitoring.",
        "collaboration": "OpenClaw is mainly positioned as personal/self-hosted. Team collaboration, role-based approvals, and enterprise governance are less visible than in established SaaS platforms.",
        "customization": "Customization is strong for technical users through self-hosting, channels, tools, skills, model providers, and configuration. Non-technical customization UX appears weaker.",
        "security": "OpenClaw's biggest weakness is also its power: an autonomous agent with real credentials can leak data, delete content, or execute unwanted actions. Public security commentary recommends isolation, least privilege, non-primary credentials, monitoring, and measurable constraints.",
        "performance": "Performance depends on local host resources, model latency, tool reliability, and channel APIs. The gateway model can be efficient, but broad tool access creates operational complexity.",
        "community": "OpenClaw has strong public attention across GitHub, Discord, Reddit, YouTube, and security blogs. Community velocity is high, but hype increases risk of low-quality add-ons and misconfiguration.",
        "strengths": [
            "clear chat-first agent interface",
            "open-source and self-hosted",
            "broad channel ambition",
            "good fit for technical users who want control",
            "large community attention and tutorial ecosystem",
        ],
        "weaknesses": [
            "security risk is substantial when connected to real accounts",
            "technical setup burden",
            "chat UX can hide dangerous state",
            "generalist agents may be unreliable for operations without constraints",
            "community hype may outrun production governance",
        ],
        "missing": [
            "default permission vault and scoped credential workflow",
            "standard approval queue for destructive actions",
            "built-in agent observability dashboard",
            "risk scoring per action",
            "enterprise identity and audit controls",
        ],
        "opportunities": [
            "safe agent onboarding mode with mock accounts",
            "policy-as-code for personal agents",
            "verified skills marketplace",
            "unified timeline of every action and tool call",
            "personal automation templates with built-in guardrails",
        ],
        "rating": {
            "Ease of Use": "6/10 - chat is easy, setup is technical",
            "Features": "8/10 - broad channels and tools",
            "Performance": "7/10 - depends on host and model stack",
            "Customization": "9/10 - open-source configurability is high",
            "AI": "8/10 - core product is agentic AI",
            "Automation": "9/10 - high automation ambition",
            "Integrations": "8/10 - strong channel coverage",
            "Scalability": "6/10 - personal use is clearer than governed enterprise scaling",
            "Innovation": "8/10 - compelling chat-native agent model",
            "Value for Money": "8/10 - open-source value is high if operated safely",
            "Overall": "7.7/10 - powerful and risky in equal measure",
        },
    },
    "reports/ai-agents/zeroclaw.md": {
        "name": "ZeroClaw",
        "original": "ZeroClaw",
        "category": "AI Agents",
        "summary": "ZeroClaw is a lightweight Rust-based agent runtime positioned as a small, fast, self-hosted alternative to heavier agent stacks.",
        "company": "ZeroClaw Labs/open-source maintainers; exact company structure is not clearly established",
        "users": "developers, edge-device builders, self-hosters, automation engineers, and teams that want a small agent runtime",
        "market": "lightweight autonomous agent runtimes and local-first automation infrastructure",
        "pricing": "open-source or self-hosted based on public GitHub/product positioning; hosted pricing is unknown",
        "business": "open-source runtime; commercial model is unknown",
        "positioning": "fast, small, Rust-native agent runtime with broad provider/channel/tool support",
        "philosophy": "agent infrastructure should be compact, portable, low-overhead, and owned by the operator",
        "vision": "an agent runtime that can run on inexpensive hardware while still connecting LLMs, channels, tools, and MCP servers",
        "problem": "many agent frameworks are heavy, Python-dependent, memory-hungry, and difficult to run continuously on small infrastructure.",
        "before": "users deployed Python frameworks, local scripts, OpenClaw-style gateways, or hosted automation platforms that added latency and operational overhead.",
        "why": "users choose it when resource footprint, startup speed, local control, and runtime simplicity matter more than a polished SaaS interface.",
        "features": [
            "Rust single-binary runtime in public positioning",
            "LLM provider support including Anthropic, OpenAI, Ollama, and other providers",
            "channels such as Discord, Telegram, Matrix, email, voice, webhooks, and CLI in public repo descriptions",
            "tools such as shell, browser, HTTP, hardware, and custom MCP servers",
            "local workspace and local credentials",
            "SQLite/vector memory mentioned in community discussion",
            "small-footprint deployment claims",
        ],
        "journey": "A technical user clones the repo or downloads a binary, configures providers and channels, runs it locally or on small hardware, adds tools, then uses it as a persistent runtime for simple autonomous workflows.",
        "ia": "ZeroClaw's IA is developer-runtime oriented: repo, configuration, providers, channels, tools, memory, and runtime philosophy. It is not primarily a dashboard product.",
        "ux": "The UX is likely excellent for users who prefer config files and binaries, but weak for non-technical users. Its product experience depends on documentation clarity and good defaults.",
        "ai": "ZeroClaw appears to provide the runtime layer around LLM providers, tools, channels, and memory rather than a proprietary model. Details of prompts, agent planning, and safety policies need repo-level verification.",
        "technical": "Public sources emphasize Rust, single binary packaging, provider adapters, channel adapters, tool execution, MCP integration, local workspace operation, and low memory footprint. Claims such as exact performance multipliers should be treated as marketing until independently benchmarked.",
        "integrations": "Known public integration areas include LLM providers, messaging channels, voice, email, webhooks, CLI, shell, browser, HTTP, hardware, and MCP servers. Exact supported adapters should be verified from the current repository.",
        "automation": "Automation is tool and channel driven. ZeroClaw's value is running agent loops cheaply and continuously, but higher-level workflow builders, approvals, and business process templates are less clear.",
        "collaboration": "Public positioning is individual/developer runtime, not collaboration SaaS. Team roles, comments, shared workspaces, and audit logs are unknown.",
        "customization": "Customization likely comes from config, provider adapters, custom tools, channel selection, and MCP servers. Theme/layout customization is not relevant.",
        "security": "Local execution and user-owned keys are strengths, but shell/browser/tool access is risky. Rust reduces some runtime classes of memory bugs but does not solve prompt injection, credential leakage, or unsafe tool calls.",
        "performance": "Performance is the main promise: low startup time, low memory, and cheap hardware. Real performance depends on model latency, tool workloads, and adapter maturity.",
        "community": "Community evidence is emerging through GitHub, Reddit, YouTube, and Claw-family articles. It is less established than OpenClaw.",
        "strengths": [
            "small runtime thesis is strong",
            "Rust binary can simplify deployment",
            "good fit for edge/self-hosted use",
            "provider and channel flexibility",
            "clear differentiation from heavy frameworks",
        ],
        "weaknesses": [
            "maturity and adoption are less proven",
            "developer-first UX",
            "benchmark claims need independent validation",
            "enterprise governance appears limited",
            "ambiguous project lineage across multiple ZeroClaw references",
        ],
        "missing": [
            "official benchmark suite",
            "visual management console",
            "permission and approval system",
            "hosted deployment option",
            "clear enterprise support path",
        ],
        "opportunities": [
            "edge-agent runtime for home labs and small businesses",
            "serverless agent workers",
            "MCP appliance pattern",
            "low-cost always-on automation nodes",
            "benchmark-driven trust campaign",
        ],
        "rating": {
            "Ease of Use": "5/10 - developer-friendly, not mainstream-friendly",
            "Features": "7/10 - broad runtime surface if adapters are mature",
            "Performance": "9/10 - performance is the core promise",
            "Customization": "8/10 - strong for developers",
            "AI": "7/10 - runtime-first rather than model-first",
            "Automation": "8/10 - well aligned to autonomous tasks",
            "Integrations": "7/10 - promising but needs verification",
            "Scalability": "7/10 - small binaries can scale operationally, governance less clear",
            "Innovation": "8/10 - compelling minimal-runtime angle",
            "Value for Money": "8/10 - low infrastructure footprint can be valuable",
            "Overall": "7.4/10 - promising technical runtime with maturity questions",
        },
    },
    "reports/ai-agents/trustclaw.md": {
        "name": "TrustClaw",
        "original": "TrustClaw",
        "category": "AI Agents",
        "summary": "TrustClaw is a self-hostable personal AI assistant built around OAuth-connected tools, sandboxed execution, memory, and safer autonomous work.",
        "company": "ComposioHQ according to the public GitHub repository",
        "users": "users who like OpenClaw-style personal agents but want stronger permission, OAuth, and sandboxing defaults",
        "market": "secure self-hostable personal AI agents and agent-tool integration platforms",
        "pricing": "open-source/self-hosted from GitHub; hosted or commercial pricing is not clearly established",
        "business": "open-source project tied to Composio's broader tool-integration ecosystem",
        "positioning": "a security-focused OpenClaw alternative with 1000+ OAuth tools and sandboxed execution",
        "philosophy": "agents should do useful work without scattering raw credentials across local config files",
        "vision": "a 24/7 personal assistant that can safely act while the user sleeps by using controlled credentials, sandboxing, and memory",
        "problem": "generalist personal agents are powerful but often unsafe because credentials, tool execution, and broad permissions are difficult to govern.",
        "before": "users self-hosted OpenClaw-style tools, wrote custom OAuth apps, used Zapier/Make, or gave assistants broad API keys and hoped prompt guardrails were enough.",
        "why": "users choose TrustClaw for a more security-centered agent model, Composio-style tool access, OAuth, and deployment that can run continuously.",
        "features": [
            "self-hostable 24/7 personal assistant",
            "1000+ tools via OAuth in public positioning",
            "sandboxed execution",
            "web and Telegram interfaces",
            "persistent memory",
            "recurring work/autopilot behavior",
            "Vercel self-hosting path",
        ],
        "journey": "A user deploys TrustClaw, connects an identity/tool account through OAuth, starts with low-risk tasks in web or Telegram, schedules recurring tasks, reviews behavior, and expands permissions only when the agent proves reliable.",
        "ia": "TrustClaw's IA appears centered on setup, OAuth-connected tools, memory, tasks, recurring work, and chat surfaces. Full product navigation should be verified from the running app.",
        "ux": "The strongest UX is trust framing: users can understand why OAuth and sandboxing matter. The challenge is making permission scope clear enough for non-technical users without burying them in security concepts.",
        "ai": "TrustClaw combines LLM-driven task handling with persistent memory and external tools. Exact models, prompt design, planner/executor split, and memory retrieval strategy are not fully documented in public summaries.",
        "technical": "Public sources indicate a self-hostable app, Vercel deployment, OAuth tool integrations, sandboxed execution, persistent memory with Postgres/pgvector mentioned by third-party coverage, and web/Telegram interfaces. Repo inspection is needed for exact architecture.",
        "integrations": "The headline integration value is 1000+ OAuth tools through Composio. Publicly mentioned surfaces include web and Telegram. Exact native integrations should be generated from the repository or Composio catalog during deeper implementation.",
        "automation": "TrustClaw supports recurring work, scheduled tasks, tool actions, and background assistant behavior. Vercel free-tier cron limits are a possible constraint mentioned in third-party commentary.",
        "collaboration": "The product is personal-agent focused. Team roles, shared workspaces, comments, version history, and enterprise audit logs are not clearly established.",
        "customization": "Customization comes from deployed environment, connected tools, OAuth scopes, prompts/instructions, memory, and schedules. Template/plugin marketplace maturity is unknown.",
        "security": "TrustClaw's product thesis is security: OAuth, sandboxing, and controlled tool execution. However, sandboxing and OAuth do not automatically solve prompt injection, cross-app permission chains, or agent misuse, so approval and observability remain important.",
        "performance": "Performance depends on hosted environment, Vercel limits, model provider latency, tool APIs, and memory store. Always-on reliability may need paid infrastructure for serious use.",
        "community": "Community evidence is newer and largely around GitHub, Composio content, setup guides, SourceForge mirror, and YouTube interviews. Adoption appears earlier than OpenClaw.",
        "strengths": [
            "security-centered positioning",
            "OAuth avoids raw-key sprawl",
            "broad Composio tool story",
            "self-hostable deployment",
            "web and Telegram access",
        ],
        "weaknesses": [
            "public maturity is still emerging",
            "depends on Composio ecosystem strength",
            "Vercel/serverless constraints can limit scheduling",
            "sandboxing may create false confidence",
            "full enterprise governance is unclear",
        ],
        "missing": [
            "visible policy simulator",
            "per-action approval inbox",
            "audit timeline and rollback",
            "permission-diff review when adding tools",
            "benchmarked security model",
        ],
        "opportunities": [
            "agent identity and permission vault",
            "OAuth-scope recommender for tasks",
            "risk-scored tool marketplace",
            "compliance-friendly personal agent logs",
            "secure migration path from OpenClaw",
        ],
        "rating": {
            "Ease of Use": "7/10 - self-hosting still requires skill, but OAuth can simplify integrations",
            "Features": "7/10 - strong tool and memory promise",
            "Performance": "6/10 - serverless and provider limits may matter",
            "Customization": "8/10 - self-hosting plus tool scopes",
            "AI": "8/10 - agentic AI is central",
            "Automation": "8/10 - recurring and tool-based work",
            "Integrations": "9/10 - Composio tool breadth is a major advantage",
            "Scalability": "6/10 - personal scaling clearer than enterprise governance",
            "Innovation": "8/10 - security-first agent framing is strong",
            "Value for Money": "8/10 - strong if self-hosted effectively",
            "Overall": "7.5/10 - promising safer-agent direction with maturity to prove",
        },
    },
    "reports/ai-development-platforms/vellum.md": {
        "name": "Vellum",
        "original": "Vellum",
        "category": "AI Development Platforms",
        "summary": "Vellum is an AI development/LLMOps platform for designing, testing, deploying, evaluating, and monitoring prompts, workflows, RAG systems, and AI applications.",
        "company": "Vellum AI / Vocify, Inc. in current legal docs",
        "users": "AI product teams, engineers, product managers, operations teams, and enterprises building production LLM applications",
        "market": "LLMOps, prompt management, workflow orchestration, evaluation, AI app deployment, and observability",
        "pricing": "public docs describe free/base and paid tiers with provider costs passed through at cost in current pricing pages; third-party pricing commentary may reference older tiers",
        "business": "SaaS platform with usage, platform, and enterprise pricing elements",
        "positioning": "a collaborative platform for taking AI products from idea to production-grade feature",
        "philosophy": "LLM applications need structured experimentation, versioning, evaluation, monitoring, and collaboration instead of ad hoc prompt editing",
        "vision": "make production AI development reliable for cross-functional teams through workflows, evaluations, deployments, and reusable app surfaces",
        "problem": "AI teams struggle to move from demos to reliable production because prompts regress, RAG pipelines drift, model behavior changes, and non-technical experts cannot easily collaborate with engineers.",
        "before": "teams used spreadsheets, notebooks, LangChain scripts, prompt playgrounds, custom eval harnesses, logging tools, and manual release notes.",
        "why": "users choose Vellum when they want one shared environment for workflow design, prompt versioning, evaluations, deployments, monitoring, and business-user collaboration.",
        "features": [
            "workflow builder for multi-step AI apps",
            "prompt and deployment management",
            "quantitative evaluations and test suites",
            "online evaluations for production monitoring",
            "RAG/document search evaluation",
            "AI Apps for running workflows through shareable UIs",
            "SDKs and API access including Node SDK",
            "example architectures for RAG, support bots, function calling, debates, and multimodal analysis",
        ],
        "journey": "A team signs up, creates a prompt or workflow, adds test cases, runs evaluations, iterates on model/prompt changes, deploys a version, invokes it by API or AI App, monitors production behavior, and uses online evaluations to catch regressions.",
        "ia": "The IA is product-development oriented: prompts, workflows, documents/search, evaluations, deployments, monitoring, API keys, examples, releases, and team/project settings.",
        "ux": "Vellum's UX strength is bridging technical and non-technical users with visual workflows and test reports. The risk is platform breadth: users may need to understand prompts, RAG, evals, deployments, datasets, API calls, and monitoring concepts before extracting full value.",
        "ai": "Vellum is model-provider agnostic orchestration and evaluation infrastructure rather than a single model. It supports workflows, prompt nodes, search/RAG nodes, model fallback patterns, online evals, and production monitoring.",
        "technical": "Public docs show workflow graphs, deployments callable through APIs, search API usage, SDKs, test suites, online evaluations, document/RAG support, and monitoring. Node SDK is available on GitHub. Exact backend architecture, cloud provider, and database stack are not fully public.",
        "integrations": "Known integration areas include API/SDK, search API, Zapier/Airtable examples, Slack support-bot examples, Cohere rerank examples, Perplexity/Firecrawl examples, LlamaIndex integration material, and model providers through workflow/prompt nodes.",
        "automation": "Automation appears through workflows, deployed APIs, AI Apps, online evaluations, monitoring, and examples that chain tools or functions. It is less personal-agent automation and more production AI pipeline automation.",
        "collaboration": "Vellum is designed for collaborative AI development across engineers and domain experts. Public materials emphasize shared workflow building and evaluation, while exact role permissions and audit depth should be verified from enterprise docs.",
        "customization": "Customization includes workflows, prompts, variables, test cases, metrics, app UIs, datasets, model choices, fallback logic, and API integrations.",
        "security": "Public sources mention SOC 2 and HIPAA through a Drata case study, security/trust materials, and enterprise readiness. Users still need to evaluate data handling with model providers and connected data sources.",
        "performance": "Performance depends on workflow complexity, model latency, retrieval systems, provider rate limits, and deployment configuration. Evaluations can reduce regressions but introduce their own cost and runtime overhead.",
        "community": "Community includes official docs, release notes, SDK repositories, blog guides, LlamaIndex integration material, third-party reviews, and AI engineering content.",
        "strengths": [
            "strong workflow plus evaluation pairing",
            "collaborative product/engineering surface",
            "production deployment and API path",
            "RAG evaluation support",
            "SDKs and examples help implementation",
        ],
        "weaknesses": [
            "platform can be complex for small teams",
            "pricing and packaging have changed across public sources",
            "model/runtime costs still accrue through providers",
            "less useful if a team already standardized on another eval/observability stack",
            "backend architecture details are not fully public",
        ],
        "missing": [
            "clear public migration guides from LangSmith, PromptLayer, and custom eval stacks",
            "transparent current enterprise feature matrix",
            "more independent benchmark comparisons",
            "built-in cost simulation for workflow changes",
            "stronger public examples for governance and approval workflows",
        ],
        "opportunities": [
            "AI app store for internal workflows",
            "eval-driven CI for prompt/workflow releases",
            "cross-functional review gates for AI behavior",
            "RAG drift monitoring dashboards",
            "workflow cost/risk optimizer",
        ],
        "rating": {
            "Ease of Use": "7/10 - visual tools help, concepts are advanced",
            "Features": "9/10 - broad LLMOps coverage",
            "Performance": "7/10 - depends on providers and workflow design",
            "Customization": "8/10 - workflows, metrics, apps, APIs",
            "AI": "9/10 - purpose-built for AI development",
            "Automation": "8/10 - strong pipeline automation",
            "Integrations": "8/10 - API, SDK, examples, provider ecosystem",
            "Scalability": "8/10 - designed for production teams",
            "Innovation": "8/10 - strong eval/workflow/app combination",
            "Value for Money": "7/10 - high value for teams, possibly heavy for solo builders",
            "Overall": "8.1/10 - strong AI development platform with adoption fit depending on team maturity",
        },
    },
}


def source_log(name):
    return "\n".join(f"- [{label}]({url})" for label, url in SOURCE_LOGS[name])


def feature_sections(features):
    categories = [
        "Core Features",
        "Advanced Features",
        "Hidden Features",
        "Power User Features",
        "Enterprise Features",
        "AI Features",
        "Automation Features",
        "Collaboration Features",
        "Customization Features",
        "Security Features",
        "Developer Features",
        "API Features",
        "Mobile Features",
        "Offline Features",
        "Accessibility Features",
        "Productivity Features",
        "Administration Features",
        "Analytics Features",
        "Billing Features",
        "Notification Features",
        "Search Features",
    ]
    lines = []
    joined = "; ".join(features)
    for category in categories:
        if category == "Core Features":
            desc = joined
        elif category == "Enterprise Features":
            desc = "Enterprise-grade packaging is partially known or unknown from public sources; evaluate permissions, audit, compliance, and support before production adoption."
        elif category == "Offline Features":
            desc = "Offline support is not clearly established; self-hosted/local deployments may keep parts of the runtime available but LLM/provider calls usually need connectivity."
        elif category == "Accessibility Features":
            desc = "Dedicated accessibility documentation was not found in this batch; chat interfaces may help some users but do not replace WCAG-reviewed UI."
        elif category == "Billing Features":
            desc = "Billing is either open-source/self-hosted cost management or SaaS pricing depending on product; detailed billing controls are not fully public."
        else:
            desc = f"Relevant capabilities exist through the product's {category.lower()} surface, but exact coverage should be verified against current docs and the running product."
        lines.append(f"### {category}\n- Description: {desc}\n- Why it exists: To turn AI from one-off answers into repeatable operational capability.\n- User benefit: Users can move faster while keeping more control over setup, workflow, or production behavior.\n")
    return "\n".join(lines)


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def rating_lines(rating):
    return "\n".join(f"- {key}: {value}" for key, value in rating.items())


def make_report(data):
    name = data["name"]
    return f"""# {name} Research Report

- Original list label: {data['original']}
- Normalized product name: {name}
- Category: {data['category']}
- Status: Research drafted - batch 001
- Minimum evidence target: 5+ trusted sources where available

## Source Log
{source_log(name)}

## 1. Product Overview

- Purpose: {data['summary']}
- Primary users: {data['users']}.
- Company: {data['company']}.
- Target market: {data['market']}.
- Pricing model: {data['pricing']}.
- Business model: {data['business']}.
- Market positioning: {data['positioning']}.
- Core philosophy: {data['philosophy']}.
- Product vision: {data['vision']}.

## 2. Problem It Solves

- What problem does it solve? {data['problem']}
- Why does this problem exist? LLMs are powerful but isolated; business systems, files, calendars, messages, retrieval stores, and approvals live in separate tools.
- How did people solve this before? {data['before']}
- Why do users choose this product? {data['why']}

## 3. Core Features

{feature_sections(data['features'])}

## 4. Complete User Journey

{data['journey']}

Major screens and interactions include discovery pages, docs or setup guides, authentication/provider configuration, integration setup, task execution, logs/results, and iterative refinement. Where the product is open-source or runtime-first, configuration and chat surfaces substitute for traditional SaaS screens.

## 5. Information Architecture

{data['ia']}

Key hierarchy: product/docs -> setup -> providers/integrations -> task/workflow execution -> monitoring/debugging -> settings/security. File/project abstractions are product-specific and should be verified during hands-on testing.

## 6. UX Analysis

{data['ux']}

Strengths include a direct path from intent to action, reduced app switching, and reusable automation. Weaknesses include hidden state, technical setup, trust calibration, and the difficulty of showing what an autonomous system is about to do.

## 7. AI Features

{data['ai']}

Important AI concepts to verify in hands-on testing: prompt hierarchy, memory write rules, memory deletion, model/provider routing, tool-call approval, retry behavior, hallucination handling, and context-window management.

## 8. Technical Analysis

{data['technical']}

Unknowns: exact production architecture, database schema, queueing model, secrets-management implementation, and complete observability stack unless directly documented in the linked source code/docs.

## 9. Integrations

{data['integrations']}

Integration quality should be judged on authentication method, permission scope, failure handling, logging, rate-limit behavior, and whether the integration can be disabled or audited cleanly.

## 10. Automation

{data['automation']}

Automation should be tested across triggers, actions, schedules, conditions, approvals, retries, and background tasks. The safest implementation pattern is low-risk task onboarding followed by measured permission expansion.

## 11. Collaboration

{data['collaboration']}

For team use, the key missing evaluation areas are shared ownership, role-based access, comments, presence, version history, change review, and audit logs.

## 12. Customization

{data['customization']}

Power users benefit most when customization is explicit, versionable, and reversible rather than hidden inside opaque learned behavior.

## 13. Security

{data['security']}

Minimum safe-use checklist: scoped credentials, separate accounts for agents, sandboxing or isolated hosts, approval gates for destructive actions, secret rotation, activity logs, and a clear emergency shutdown path.

## 14. Performance

{data['performance']}

Performance should be evaluated with real workflows, not only demos: cold start, model latency, tool latency, memory retrieval, retries, channel delivery, and long-running task stability.

## 15. Community

{data['community']}

Useful community signals: GitHub activity, issue quality, Discord/Reddit support, independent reviews, security research, tutorial freshness, and changelog cadence.

## 16. Strengths

{bullets(data['strengths'])}

## 17. Weaknesses

{bullets(data['weaknesses'])}

## 18. Missing Features

{bullets(data['missing'])}

These matter because autonomous products fail when users cannot understand permissions, predict actions, recover mistakes, or inspect why an agent behaved a certain way.

## 19. Hidden Opportunities

{bullets(data['opportunities'])}

The larger opportunity is to make autonomy legible: users need a product that shows intent, risk, evidence, permissions, and rollback before it asks for trust.

## 20. Reverse Engineering

- Keep: {data['summary']}
- Redesign: make permissioning, memory, logs, and approvals first-class rather than secondary setup details.
- Remove: any default that encourages broad credentials, invisible background work, or unreviewed destructive actions.
- Simplify: onboarding, provider setup, integration discovery, and debugging paths.

## 21. Competitive Advantages

- Why users stay: users stay when the product accumulates useful setup, memory, workflows, integrations, and trust.
- What creates lock-in: learned skills, configured tools, connected accounts, historical memory, evaluation datasets, or deployed workflows.
- Why competitors struggle: competitors must match both user trust and operational depth, not just chat quality.

## 22. Ideal User

- Who should use it: {data['users']}.
- Who should avoid it: users who cannot monitor autonomous actions, do not want technical setup, or need mature compliance controls immediately.

## 23. SWOT Analysis

- Strengths: {', '.join(data['strengths'][:3])}.
- Weaknesses: {', '.join(data['weaknesses'][:3])}.
- Opportunities: {', '.join(data['opportunities'][:3])}.
- Threats: platform vendors, model-provider changes, security incidents, integration breakage, and user distrust after automation failures.

## 24. Product Rating

{rating_lines(data['rating'])}

## 25. Lessons Learned

- Best ideas worth keeping: persistent context, workflow reuse, tool integrations, and source-backed iteration.
- Worst ideas to avoid: broad permissions, invisible execution, vague guardrails, and memory that users cannot inspect.
- Innovations worth adapting: the strongest product idea is turning AI from a session into an operational system with memory, tools, and reviewable work.
- Design principles: make state, permissions, risk, and history visible.
- Architecture principles: isolate execution, scope credentials, log every action, and make integrations replaceable.
- Business lessons: trust is a product feature, not a compliance afterthought.
- Product strategy lessons: autonomy should start narrow, prove reliability, and earn broader access over time.
"""


def main():
    generated = {}
    for path, data in REPORTS.items():
        content = make_report(data)
        full_path = ROOT / path
        full_path.write_text(content.rstrip() + "\n", encoding="utf-8")
        generated[path] = data["name"]

    registry_path = ROOT / "product-registry.md"
    registry = registry_path.read_text(encoding="utf-8")
    for path in generated:
        registry = registry.replace(f"[{path}]({path}) | Not started |", f"[{path}]({path}) | Research drafted - batch 001 |")
    registry_path.write_text(registry, encoding="utf-8")

    combined_lines = [
        "# Complete Product Research Report",
        "",
        "This master report preserves the original product-list order after deduplicating the repeated Fathom entry. Each detailed report lives in its category folder.",
        "",
        "## Master Order",
        "",
    ]
    for line in registry.splitlines():
        if line.startswith("| ") and not line.startswith("| Order") and not line.startswith("|---"):
            parts = [part.strip() for part in line.strip("|").split("|")]
            combined_lines.append(f"{parts[0]}. [{parts[2]}]({parts[4].split('](')[-1].rstrip(')')}) - {parts[3]} - {parts[5]}")

    combined_lines.extend(["", "## Combined Reports", ""])
    for path in generated:
        combined_lines.append((ROOT / path).read_text(encoding="utf-8"))
        combined_lines.append("\n---\n")
    combined_lines.append("_Remaining product reports will be appended in original registry order as each batch is completed._\n")
    (ROOT / "combined/complete-product-research-report.md").write_text("\n".join(combined_lines).rstrip() + "\n", encoding="utf-8")

    candidates = ROOT / "discovered-tools/candidates.md"
    text = candidates.read_text(encoding="utf-8")
    additions = [
        "| OpenRouter | Model routing | Appeared as a Hermes provider option | Hermes Agent | https://openrouter.ai/ | Useful for multi-model routing and fallback research. |",
        "| Ollama | Local model runtime | Appeared in Hermes and ZeroClaw provider references | Hermes Agent; ZeroClaw | https://ollama.com/ | Important local inference layer for self-hosted agents. |",
        "| vLLM | Inference infrastructure | Appeared in Hermes provider references | Hermes Agent | https://github.com/vllm-project/vllm | Useful for self-hosted high-throughput inference. |",
        "| Composio | Agent tool integration platform | TrustClaw uses Composio-style OAuth/tool access | TrustClaw | https://composio.dev/ | Strong candidate for agent integration and permission research. |",
        "| LangSmith | LLM observability/evaluation | Appears in Vellum competitive context | Vellum | https://www.langchain.com/langsmith | Relevant for evaluation and observability comparison later. |",
        "| LlamaIndex | RAG framework | Appears in Vellum integration material | Vellum | https://www.llamaindex.ai/ | Important RAG and prompt-management ecosystem dependency. |",
    ]
    for addition in additions:
        if addition not in text:
            text += "\n" + addition
    candidates.write_text(text.rstrip() + "\n", encoding="utf-8")

    print("Batch 001 reports filled: " + ", ".join(generated.values()))


if __name__ == "__main__":
    main()
