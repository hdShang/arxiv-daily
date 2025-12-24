---
layout: default
title: "RedCoder: Automated Multi-Turn Red Teaming for Code LLMs"
---

# RedCoder: Automated Multi-Turn Red Teaming for Code LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.22063" class="toolbar-btn" target="_blank">📄 arXiv: 2507.22063v1</a>
  <a href="https://arxiv.org/pdf/2507.22063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.22063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.22063v1', 'RedCoder: Automated Multi-Turn Red Teaming for Code LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Jacky Mo, Qin Liu, Xiaofei Wen, Dongwon Jung, Hadi Askari, Wenxuan Zhou, Zhe Zhao, Muhao Chen

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出RedCoder以解决代码生成模型的安全性评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `红队` `代码生成` `安全评估` `多轮对话` `大型语言模型` `自动化测试` `脆弱性诱导`

## 📋 核心要点

1. 现有红队方法依赖大量人力，难以扩展，且忽视了多轮交互的特性，导致评估效率低下。
2. RedCoder通过多轮对话与代码生成模型互动，自动引导生成脆弱代码，提升了红队的效率和效果。
3. 实验结果显示，RedCoder在诱导代码脆弱性方面显著优于传统方法，展示了其在安全评估中的潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码生成方面展现了卓越的能力，但在对抗性环境中，它们容易生成脆弱或恶意代码。现有的红队方法依赖大量人力，限制了其可扩展性，并且通常忽视了现实世界中AI辅助编程的多轮交互特性。为了解决这些问题，本文提出了RedCoder，一个能够与受害模型进行多轮对话以引导生成脆弱代码的红队代理。RedCoder的构建流程始于多代理游戏过程，模拟对抗性互动，生成原型对话和可重用的攻击策略。通过在这些原型对话上微调LLM，RedCoder能够自主与代码LLM进行多轮对话，动态检索相关策略，引导对话朝向脆弱性输出。实验结果表明，该方法在诱导代码生成中的脆弱性方面优于以往的单轮和多轮红队方法，提供了一种可扩展且有效的工具来评估现代代码生成系统的安全边界。

## 🔬 方法详解

**问题定义**：本文旨在解决现有红队方法在评估代码生成模型安全性时的低效和不可扩展性问题，尤其是在多轮交互场景下的不足。

**核心思路**：RedCoder的核心思路是通过模拟多轮对话的方式，与代码生成模型进行互动，自动引导其生成脆弱代码，从而提高红队的效率和效果。

**技术框架**：RedCoder的构建流程包括多代理游戏过程、原型对话生成和LLM微调三个主要阶段。首先，通过多代理游戏模拟对抗性互动，生成原型对话和攻击策略；然后，微调LLM以支持多轮对话；最后，RedCoder能够自主进行对话并引导输出。

**关键创新**：RedCoder的主要创新在于其多轮对话能力，能够动态检索攻击策略并引导对话，显著提高了诱导脆弱性的效率，与传统的单轮红队方法形成鲜明对比。

**关键设计**：在设计上，RedCoder使用了特定的损失函数和网络结构，以确保在多轮对话中能够有效地引导生成脆弱代码，同时保持对话的连贯性和相关性。

## 📊 实验亮点

实验结果表明，RedCoder在诱导代码脆弱性方面的表现优于以往的单轮和多轮红队方法，具体提升幅度达到XX%（具体数据未知），展示了其在评估现代代码生成系统安全性方面的有效性和可扩展性。

## 🎯 应用场景

RedCoder的研究成果在软件开发和安全测试领域具有广泛的应用潜力。它可以作为评估代码生成模型安全性的工具，帮助开发者识别潜在的安全漏洞，从而提升软件的安全性。此外，RedCoder的多轮对话能力也可以应用于其他需要人机交互的领域，如智能助手和自动化测试。未来，随着代码生成技术的不断发展，RedCoder有望成为安全评估的标准工具。

## 📄 摘要（原文）

> Large Language Models (LLMs) for code generation (i.e., Code LLMs) have demonstrated impressive capabilities in AI-assisted software development and testing. However, recent studies have shown that these models are prone to generating vulnerable or even malicious code under adversarial settings. Existing red-teaming approaches rely on extensive human effort, limiting their scalability and practicality, and generally overlook the interactive nature of real-world AI-assisted programming, which often unfolds over multiple turns. To bridge these gaps, we present RedCoder, a red-teaming agent that engages victim models in multi-turn conversation to elicit vulnerable code. The pipeline to construct RedCoder begins with a multi-agent gaming process that simulates adversarial interactions, yielding a set of prototype conversations and an arsenal of reusable attack strategies. We then fine-tune an LLM on these prototype conversations to serve as the backbone of RedCoder. Once deployed, RedCoder autonomously engages Code LLMs in multi-turn conversations, dynamically retrieving relevant strategies from the arsenal to steer the dialogue toward vulnerability-inducing outputs. Experiments across multiple Code LLMs show that our approach outperforms prior single-turn and multi-turn red-team methods in inducing vulnerabilities in code generation, offering a scalable and effective tool for evaluating the security boundaries of modern code-generation systems.

