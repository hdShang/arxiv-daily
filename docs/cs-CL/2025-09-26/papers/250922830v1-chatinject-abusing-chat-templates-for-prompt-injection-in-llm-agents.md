---
layout: default
title: "ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents"
---

# ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22830" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22830v1</a>
  <a href="https://arxiv.org/pdf/2509.22830.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22830v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22830v1', 'ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hwan Chang, Yonghyun Jun, Hwanhee Lee

**分类**: cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**ChatInject：利用聊天模板在LLM Agent中进行提示注入攻击**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `提示注入` `聊天模板` `安全漏洞` `对抗攻击`

## 📋 核心要点

1. 现有LLM Agent易受间接提示注入攻击，攻击者可利用外部环境输出中的恶意指令控制Agent行为。
2. ChatInject攻击通过模仿原生聊天模板格式化恶意payload，利用LLM的指令遵循特性实现注入。
3. 实验表明ChatInject显著提升了攻击成功率，且具有跨模型迁移性，现有防御措施效果不佳。

## 📝 摘要（中文）

基于大型语言模型（LLM）的Agent与外部环境交互的日益普及，为对抗性操纵创造了新的攻击面。其中一个主要威胁是间接提示注入，攻击者将恶意指令嵌入到外部环境的输出中，导致Agent将其解释并执行为合法的提示。先前的研究主要集中在纯文本注入攻击上，而我们发现了一个重要但未被充分探索的漏洞：LLM对结构化聊天模板的依赖性以及它们通过有说服力的多轮对话进行上下文操纵的敏感性。为此，我们引入了ChatInject，一种将恶意payload格式化为模仿原生聊天模板的攻击，从而利用模型固有的指令遵循倾向。在此基础上，我们开发了一种基于说服的多轮变体，通过对话轮次来引导Agent接受并执行原本可疑的操作。通过对前沿LLM的全面实验，我们证明了三个关键发现：（1）ChatInject实现了比传统提示注入方法显著更高的平均攻击成功率，在AgentDojo上从5.18%提高到32.05%，在InjecAgent上从15.13%提高到45.90%，其中多轮对话在InjecAgent上表现出特别强的性能，平均成功率为52.33%；（2）基于聊天模板的payload表现出强大的跨模型迁移性，即使对于闭源LLM也有效，尽管它们的模板结构未知；（3）现有的基于提示的防御措施对这种攻击方法基本无效，特别是对多轮变体。这些发现突出了当前Agent系统中的漏洞。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM Agent中存在的间接提示注入漏洞，特别是利用聊天模板进行攻击的问题。现有方法主要关注纯文本注入，忽略了LLM对结构化聊天模板的依赖性，以及通过多轮对话进行上下文操纵的可能性。

**核心思路**：核心思路是利用LLM对聊天模板的固有依赖性，构造恶意payload，使其看起来像是合法的聊天消息，从而诱导Agent执行恶意指令。通过模仿聊天模板的结构，攻击者可以绕过一些简单的防御机制，并提高攻击的成功率。

**技术框架**：ChatInject攻击主要分为两个阶段：单轮攻击和多轮攻击。单轮攻击直接构造模仿聊天模板的恶意payload。多轮攻击则通过多轮对话，逐步引导Agent进入攻击者设定的情境，最终执行恶意指令。多轮攻击的关键在于设计具有说服力的对话策略，使Agent逐渐接受攻击者的指令。

**关键创新**：关键创新在于发现了LLM Agent对聊天模板的依赖性，并利用这一特性设计了ChatInject攻击。与传统的纯文本注入攻击相比，ChatInject攻击更具隐蔽性和有效性，能够绕过一些简单的防御机制。多轮攻击进一步增强了攻击的成功率，使其能够应对更复杂的防御策略。

**关键设计**：ChatInject攻击的关键设计在于payload的构造，需要精确模仿目标LLM的聊天模板。对于闭源LLM，可以通过试错的方式推断其聊天模板结构。多轮攻击的关键在于设计具有说服力的对话策略，可以使用强化学习等方法来优化对话策略，提高攻击的成功率。论文中没有明确提及具体的参数设置、损失函数或网络结构，这部分细节可能需要进一步研究。

## 📊 实验亮点

实验结果表明，ChatInject攻击在AgentDojo和InjecAgent上的平均攻击成功率分别从5.18%提高到32.05%和从15.13%提高到45.90%。多轮对话攻击在InjecAgent上达到了52.33%的平均成功率。此外，ChatInject攻击具有很强的跨模型迁移性，即使对于闭源LLM也有效。现有的基于提示的防御措施对ChatInject攻击基本无效，特别是对多轮攻击。

## 🎯 应用场景

该研究成果可应用于评估和提升LLM Agent的安全性，帮助开发者识别和修复潜在的提示注入漏洞。此外，该研究也为开发更有效的防御机制提供了思路，例如，通过检测和过滤恶意聊天模板，或者通过增强LLM对上下文的理解能力，从而降低提示注入攻击的风险。未来的研究可以探索更复杂的攻击场景和防御策略。

## 📄 摘要（原文）

> The growing deployment of large language model (LLM) based agents that interact with external environments has created new attack surfaces for adversarial manipulation. One major threat is indirect prompt injection, where attackers embed malicious instructions in external environment output, causing agents to interpret and execute them as if they were legitimate prompts. While previous research has focused primarily on plain-text injection attacks, we find a significant yet underexplored vulnerability: LLMs' dependence on structured chat templates and their susceptibility to contextual manipulation through persuasive multi-turn dialogues. To this end, we introduce ChatInject, an attack that formats malicious payloads to mimic native chat templates, thereby exploiting the model's inherent instruction-following tendencies. Building on this foundation, we develop a persuasion-driven Multi-turn variant that primes the agent across conversational turns to accept and execute otherwise suspicious actions. Through comprehensive experiments across frontier LLMs, we demonstrate three critical findings: (1) ChatInject achieves significantly higher average attack success rates than traditional prompt injection methods, improving from 5.18% to 32.05% on AgentDojo and from 15.13% to 45.90% on InjecAgent, with multi-turn dialogues showing particularly strong performance at average 52.33% success rate on InjecAgent, (2) chat-template-based payloads demonstrate strong transferability across models and remain effective even against closed-source LLMs, despite their unknown template structures, and (3) existing prompt-based defenses are largely ineffective against this attack approach, especially against Multi-turn variants. These findings highlight vulnerabilities in current agent systems.

