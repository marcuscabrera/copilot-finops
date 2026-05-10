# FinOps Agent — Microsoft Copilot Studio Sample

> A production-ready **FinOps Advisor agent** built with Microsoft Copilot Studio. Helps organizations understand, manage, and optimize Microsoft cloud spending across Azure, Microsoft 365, Copilot, AI Foundry, and Fabric — grounded in official Microsoft Learn documentation.

<p align="center">
  <img src="FinOps Agent/icon.png" alt="FinOps Agent Icon" width="120" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/renatoromao/">
    <img src="https://img.shields.io/badge/LinkedIn-Follow%20Renato%20Romão-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/Platform-Microsoft%20Copilot%20Studio-742774?style=for-the-badge&logo=microsoftcopilot&logoColor=white" alt="Copilot Studio" />
  &nbsp;
  <img src="https://img.shields.io/badge/Model-Claude%20Sonnet%204.6-FF6B00?style=for-the-badge&logo=anthropic&logoColor=white" alt="Model" />
</p>

<img width="1462" height="775" alt="image" src="https://github.com/user-attachments/assets/47249da6-dab2-40b3-9cd9-68e63f0c999d" />

<img width="1454" height="769" alt="image" src="https://github.com/user-attachments/assets/fe1d5d3b-6556-4c55-9b15-9fef2f422228" />

---

## 📋 Table of Contents

- [Description](#description)
- [Technologies & Frameworks](#technologies--frameworks)
- [Installation & Configuration](#installation--configuration)
- [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact & Support](#contact--support)
- [Roadmap](#roadmap)

---

## Description

The **FinOps Agent** is an intelligent conversational agent built with **Microsoft Copilot Studio** that applies [FinOps Foundation](https://www.finops.org/) principles to Microsoft cloud services. It provides instant, actionable guidance on cloud cost management and optimization, all grounded in official Microsoft Learn documentation.

### Key Features

| Domain | Coverage |
|---|---|
| **Azure Cost Management** | Budgets, alerts, reservations, savings plans, right-sizing |
| **Microsoft 365** | E3/E5 licensing, license optimization, usage analytics |
| **Microsoft Copilot** | M365 Copilot licensing, Copilot Studio consumption billing, ROI |
| **Microsoft Foundry** | Token-based pricing, model deployment costs, AI workload optimization |
| **Microsoft Fabric** | Capacity units, workload cost management, reserved capacity |
| **FinOps Best Practices** | Chargeback/showback, tagging, budgeting, forecasting, cost allocation |

All answers are **grounded in official Microsoft Learn documentation** through semantic search — no hallucinations, no guesswork.

---

## Technologies & Frameworks

| Category | Technology | Version/Details |
|---|---|---|
| **Platform** | Microsoft Copilot Studio | Cloud-based conversational AI platform |
| **Programming Language** | YAML | `.mcs.yml` configuration files |
| **AI Model** | Claude Sonnet 4.6 | Anthropic large language model |
| **Framework** | Adaptive Dialog | Microsoft Conversational AI framework |
| **Authentication** | OAuth 2.0 / Integrated Auth | Microsoft 365 authentication |
| **Knowledge Sources** | Microsoft Learn APIs | 6 official documentation sources |
| **Search Engine** | Semantic Search | Azure AI-powered semantic search |
| **Development Tools** | VS Code + Copilot Studio Extension | Local development and deployment |
| **Version Control** | Git | Source code management |

### Dependencies

- Microsoft 365 tenant with Copilot Studio license
- Copilot Studio VS Code extension (latest version)
- Visual Studio Code (latest stable)
- Git (latest version)

---

## Installation & Configuration

### Prerequisites

Before deploying the FinOps Agent, ensure you have:

- [x] A **Microsoft 365 tenant** with an active Copilot Studio license
- [x] **Copilot Studio** access ([aka.ms/copilotstudio](https://aka.ms/copilotstudio))
- [x] **Visual Studio Code** installed (latest stable version)
- [x] **Copilot Studio VS Code extension** installed ([download here](https://marketplace.visualstudio.com/items?itemName=ms-CopilotStudio.vscode-copilotstudio))
- [x] **Git** installed locally

### Step-by-Step Installation

#### Step 1 — Clone This Repository

```bash
git clone https://github.com/renatoromao/copilotstudio-samples-finops.git
cd copilotstudio-samples-finops
```

#### Step 2 — Open in VS Code

```bash
code .
```

#### Step 3 — Create a New Agent in Copilot Studio

1. Navigate to [Copilot Studio](https://aka.ms/copilotstudio) and sign in with your Microsoft 365 account
2. Click **Create** → **New agent**
3. Provide a name (e.g., _My FinOps Agent_) and complete the setup wizard
4. Once created, note the agent name for the next step

#### Step 4 — Clone Your Agent Locally via VS Code Extension

1. In VS Code, open the **Copilot Studio** panel from the Activity Bar (left sidebar)
2. Click **Sign in** and authenticate with your Microsoft 365 credentials
3. Select the **Environment** where you created the agent
4. Find your agent in the list and click **Clone** (or **Open locally**) to download it to your local machine

#### Step 5 — Copy FinOps Agent Files

Copy the following files from this repository into your locally cloned agent folder, **replacing** existing files:

```
FinOps Agent/
├── agent.mcs.yml        ← Copy and replace
├── settings.mcs.yml     ← Copy and replace (optional, review first)
├── knowledge/           ← Copy entire folder and replace
└── topics/              ← Copy entire folder and replace
```

> 💡 **Tip**: Review `settings.mcs.yml` before replacing if you have custom authentication or access control requirements.

#### Step 6 — Apply Changes via the Extension

1. In VS Code, open the **Copilot Studio** panel
2. Click **Apply Changes** (or **Publish**) to push your local changes to Copilot Studio
3. Wait for confirmation that changes were applied successfully

#### Step 7 — Configure Authentication (Optional)

If your organization requires specific authentication settings:

1. Open `settings.mcs.yml`
2. Modify the `authenticationMode` and `authenticationTrigger` as needed
3. Configure `accessControlPolicy` based on your security requirements

Available authentication modes:
- `Integrated` — Uses Microsoft 365 integrated authentication
- `Anonymous` — No authentication required (not recommended for production)

#### Step 8 — Test in Copilot Studio

1. Open [Copilot Studio](https://aka.ms/copilotstudio) and navigate to your agent
2. Click **Test** in the top-right corner to open the test chat panel
3. Start a conversation and validate the agent's responses

---

## Usage Examples

Once deployed, interact with the FinOps Agent using natural language queries. Here are example prompts organized by category:

### Azure Cost Management

```
"What is the best Azure savings plan for a predictable workload?"
"How do I set up a budget alert in Azure Cost Management?"
"Explain the difference between Azure Reserved Instances and Savings Plans"
"What are the steps to right-size underutilized Azure VMs?"
```

### Microsoft 365 Licensing

```
"What's the difference between Microsoft 365 E3 and E5 from a cost perspective?"
"How can I optimize M365 license assignment to reduce costs?"
"What tools are available to analyze M365 license usage?"
```

### Microsoft Copilot

```
"How is Microsoft Copilot Studio billed?"
"What is the pricing model for M365 Copilot?"
"How do I calculate ROI for Copilot deployment?"
```

### Microsoft Fabric

```
"How do I optimize Microsoft Fabric capacity costs?"
"What are Fabric Capacity Units (CUs) and how are they priced?"
"Should I use reserved capacity for Fabric workloads?"
```

### Microsoft AI Foundry

```
"What is the token-based pricing model for Azure AI Foundry?"
"How can I optimize costs for AI model deployments?"
"What are the cost considerations for different foundation models?"
```

### General FinOps Practices

```
"How do I implement a chargeback model for cloud costs?"
"What is a good tagging strategy for cost allocation?"
"How do I create a cloud budget forecast?"
"Explain the FinOps framework phases"
```

### Expected Response Format

The agent provides structured responses with:

- ✅ **Grounded citations** from official Microsoft Learn documentation
- 📊 **Actionable recommendations** with specific steps
- ⚠️ **Cost disclaimers** noting regional and agreement variations
- 🔗 **Direct links** to relevant documentation and pricing calculators

Example response structure:

```markdown
## Azure Savings Plans for Predictable Workloads

For predictable, consistent workloads, **Azure Savings Plans** offer:

### Benefits
- Up to 65% savings compared to pay-as-you-go pricing
- Flexibility across VM families, regions, and sizes
- No upfront commitment required

### Recommendation Steps
1. Analyze your usage patterns in Azure Cost Management
2. Identify baseline consumption (minimum consistent usage)
3. Purchase a 1-year or 3-year Savings Plan...

📖 **Source**: [Azure Savings Plans Documentation](https://learn.microsoft.com/azure/cost-management-billing/reservations/savings-plan...)

💡 **Note**: Actual savings vary by region, VM series, and term length. Use the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) for precise estimates.
```

---

## Project Structure

```
FinOps Agent/
├── agent.mcs.yml                    # Core agent configuration, instructions & AI model settings
├── settings.mcs.yml                 # Access control, authentication, and generative AI features
├── icon.png                         # Agent icon (512×512 PNG recommended)
│
├── knowledge/                       # 6 Microsoft Learn knowledge sources
│   ├── azure-cost-management-billing.knowledge.mcs.yml
│   ├── finops-with-azure.knowledge.mcs.yml
│   ├── azure-ai-foundry.knowledge.mcs.yml
│   ├── copilot-for-microsoft-365.knowledge.mcs.yml
│   ├── microsoft-365-licensing-pricing.knowledge.mcs.yml
│   └── microsoft-fabric-pricing-capacity.knowledge.mcs.yml
│
└── topics/                          # 13 conversation topics (Adaptive Dialog flows)
    ├── ConversationStart.mcs.yml    # Triggers when conversation begins
    ├── Search.mcs.yml               # Main knowledge search with conversational boosting
    ├── Greeting.mcs.yml             # Handles user greetings
    ├── Fallback.mcs.yml             # Handles unrecognized intents
    ├── Escalate.mcs.yml             # Human hand-off scenarios
    ├── Goodbye.mcs.yml              # Conversation closure
    ├── EndofConversation.mcs.yml    # Post-conversation actions (CSAT, telemetry)
    ├── OnError.mcs.yml              # Error handling and recovery
    ├── Signin.mcs.yml               # Authentication flow
    ├── ThankYou.mcs.yml             # Acknowledges user gratitude
    ├── StartOver.mcs.yml            # Resets conversation context
    ├── ResetConversation.mcs.yml    # Clears conversation history
    └── MultipleTopicsMatched.mcs.yml # Disambiguation when multiple topics match
```

### File Descriptions

| File | Purpose |
|---|---|
| `agent.mcs.yml` | Defines agent persona, instructions, scope, capabilities (web browsing), and AI model (Claude Sonnet 4.6) |
| `settings.mcs.yml` | Configures authentication mode, access control policy, generative AI capabilities, and recognizer type |
| `knowledge/*.yml` | Each file configures a semantic search source pointing to official Microsoft Learn documentation URLs |
| `topics/*.yml` | Adaptive Dialog definitions for handling specific conversation scenarios and user intents |

---

## Contributing

We welcome contributions from the community! This section provides guidelines for contributing to the FinOps Agent project.

### Code of Conduct

Please be respectful and professional in all interactions. This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

### How to Contribute

1. **Fork the Repository**
   - Click the "Fork" button at the top right of the repository page
   - Clone your fork locally: `git clone https://github.com/YOUR_USERNAME/copilotstudio-samples-finops.git`

2. **Create a Branch**
   - Create a branch for your feature or fix: `git checkout -b feature/your-feature-name`
   - Use descriptive branch names (e.g., `feature/add-new-knowledge-source`, `fix/typo-in-instructions`)

3. **Make Your Changes**
   - Follow the existing YAML structure and formatting
   - Add comments to explain complex configurations
   - Test your changes in Copilot Studio before submitting

4. **Style Guidelines**
   - **YAML Formatting**: Use 2-space indentation consistently
   - **Comments**: Add descriptive comments using `#` for all configuration files
   - **Naming Conventions**: Use kebab-case for file names (e.g., `azure-cost-management.mcs.yml`)
   - **Documentation**: Update this README if you add new features or change functionality

5. **Test Your Changes**
   - Deploy your modified agent to a test environment in Copilot Studio
   - Verify all conversation topics work as expected
   - Test with various user queries to ensure quality responses

6. **Submit a Pull Request**
   - Push your changes: `git push origin feature/your-feature-name`
   - Open a Pull Request (PR) from your fork to the main repository
   - Fill out the PR template with:
     - Clear description of changes
     - Motivation for the change
     - Testing performed
     - Screenshots (if applicable)

### Pull Request Process

1. **Review**: All PRs are reviewed by the maintainers within 5-7 business days
2. **Feedback**: Address any feedback or requested changes promptly
3. **Approval**: Once approved, a maintainer will merge your PR
4. **Release**: Changes are typically included in the next release cycle

### What We're Looking For

- ✅ New knowledge sources (additional Microsoft Learn documentation URLs)
- ✅ Improved conversation topics and dialog flows
- ✅ Bug fixes and error handling improvements
- ✅ Documentation enhancements
- ✅ Security improvements
- ✅ Performance optimizations

### Reporting Issues

Found a bug or have a feature request? Please open an issue on GitHub with:
- Clear title and description
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Environment details (Copilot Studio version, etc.)

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

You are free to:
- ✅ Use this project for commercial purposes
- ✅ Modify and distribute the code
- ✅ Use it in private projects

Required:
- 📄 Include the original license and copyright notice in any distributions

```
Copyright (c) Renato Romão

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact & Support

### Author

**Renato Romão**  
6x Microsoft MVP (Copilot Studio & Microsoft Foundry)

| Platform | Link |
|---|---|
| 🔗 LinkedIn | [Follow Renato Romão](https://www.linkedin.com/in/renatoromao/) |
| 📧 Email | Available via LinkedIn |
| 🌐 Website | Check LinkedIn for latest info |

### Getting Help

- **General Questions**: Open a [GitHub Discussion](https://github.com/renatoromao/copilotstudio-samples-finops/discussions)
- **Bug Reports**: Open a [GitHub Issue](https://github.com/renatoromao/copilotstudio-samples-finops/issues)
- **Copilot Studio Documentation**: [Official Microsoft Docs](https://learn.microsoft.com/en-us/microsoft-copilot-studio/)
- **FinOps Foundation**: [www.finops.org](https://www.finops.org/)

### Office Hours

For enterprise inquiries or consultation requests, please reach out via LinkedIn with a brief description of your needs.

---

## Roadmap

Here's what's planned for future releases of the FinOps Agent:

### Q2 2025 (Current Quarter)

| Feature | Status | Priority |
|---|---|---|
| Multi-language support (Spanish, Portuguese, French) | 📋 Planned | High |
| Custom cost calculator integration | 🔄 In Progress | High |
| Enhanced escalation workflows with Teams integration | 📋 Planned | Medium |
| Power BI dashboard templates for cost analytics | 📋 Planned | Medium |

### Q3 2025

| Feature | Status | Priority |
|---|---|---|
| Azure Cost Management API integration for live data* | 📋 Planned | High |
| Custom connector for third-party FinOps tools | 📋 Planned | Medium |
| Advanced analytics and conversation insights | 📋 Planned | Medium |
| Mobile-optimized test canvas experience | 📋 Planned | Low |

### Q4 2025 & Beyond

| Feature | Status | Priority |
|---|---|---|
| AWS and GCP cost management knowledge sources | 💡 Considering | Medium |
| Automated cost anomaly detection alerts | 💡 Considering | High |
| Integration with Azure Advisor recommendations | 💡 Considering | High |
| Custom branding and white-labeling options | 💡 Considering | Low |

> *Live data integration requires additional authentication and subscription access configuration.*

### How You Can Help

We prioritize features based on community feedback! Let us know what's most important to you:

1. 👍 React to existing roadmap items on GitHub
2. 💬 Comment on planned features with your use cases
3. 🆕 Submit new feature requests with detailed scenarios
4. 🤝 Contribute code for features you need urgently

---

## Part of the Copilot Studio Samples Collection

This repo is part of a growing collection of **Microsoft Copilot Studio sample agents** — each in its own repository, ready to clone and deploy.

> **More samples coming soon.** Follow along to be notified when new agents drop.

### Other Sample Agents

| Agent | Description | Repository |
|---|---|---|
| HR Assistant | Employee onboarding, policy Q&A | Coming Soon |
| IT Helpdesk | Technical support ticket routing | Coming Soon |
| Sales Coach | Sales methodology and best practices | Coming Soon |

---

<p align="center">
  Made with ❤️ for the Microsoft community
</p>

---

**Last Updated**: May 2025

