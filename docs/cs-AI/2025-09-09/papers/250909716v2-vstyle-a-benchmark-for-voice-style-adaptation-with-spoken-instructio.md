---
layout: default
title: "VStyle: A Benchmark for Voice Style Adaptation with Spoken Instructions"
---

# VStyle: A Benchmark for Voice Style Adaptation with Spoken Instructions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09716" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09716v2</a>
  <a href="https://arxiv.org/pdf/2509.09716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09716v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09716v2', 'VStyle: A Benchmark for Voice Style Adaptation with Spoken Instructions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Zhan, Mingyang Han, Yuxuan Xie, Chen Wang, Dong Zhang, Kexin Huang, Haoxiang Shi, DongXiao Wang, Tengtao Song, Qinyuan Cheng, Shimin Li, Jun Song, Xipeng Qiu, Bo Zheng

**分类**: cs.SD, cs.AI, cs.CL, eess.AS

**发布日期**: 2025-09-09 (更新: 2025-09-22)

**🔗 代码/项目**: [PROJECT_PAGE](https://junzhan2000.github.io/VStyle.github.io/)

---

## 💡 一句话要点

**VStyle：一个基于口语指令的语音风格迁移评测基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音风格迁移` `口语语言模型` `评测基准` `语音生成` `人机交互`

## 📋 核心要点

1. 现有口语语言模型在语音风格迁移方面能力不足，难以根据口语指令调整音色、韵律等。
2. 论文提出VStyle基准，包含声学属性、自然语言指令等四类任务，用于评估模型风格迁移能力。
3. 引入LALM作为评判器框架，从文本忠实度、风格一致性和自然度三方面客观评估模型输出。

## 📝 摘要（中文）

口语语言模型（SLM）已成为语音理解和生成的一种统一范式，实现了自然的人机交互。然而，虽然大多数进展都集中在语义准确性和指令遵循上，但SLM基于口语指令调整其说话风格的能力受到的关注有限。我们引入了语音风格迁移（VSA）这一新任务，旨在考察SLM是否能够根据自然语言口语命令修改其说话风格，例如音色、韵律或角色。为了研究这个任务，我们提出了VStyle，一个双语（中文和英文）评测基准，涵盖了四类语音生成：声学属性、自然语言指令、角色扮演和隐式共情。我们还引入了大型音频语言模型作为评判器（LALM as a Judge）框架，该框架逐步评估输出的文本忠实度、风格一致性和自然度，确保可重复和客观的评估。对商业系统和开源SLM的实验表明，当前模型在可控风格迁移方面面临明显的局限性，突出了这项任务的新颖性和挑战性。通过发布VStyle及其评估工具包，我们旨在为社区提供一个推进以人为中心的口语交互的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决口语语言模型（SLM）在语音风格迁移（VSA）方面的不足。现有SLM主要关注语义准确性和指令遵循，而忽略了根据口语指令调整语音风格（如音色、韵律、角色）的能力。这限制了人机交互的自然性和表现力。

**核心思路**：论文的核心思路是构建一个全面的评测基准VStyle，用于系统性地评估SLM在VSA任务上的表现。同时，引入LALM作为评判器，以客观、可重复的方式评估模型的输出质量。通过基准测试和评估，可以促进SLM在语音风格控制方面的研究和发展。

**技术框架**：VStyle基准包含四个主要类别：1) 声学属性控制，要求模型根据指令调整语音的声学特征；2) 自然语言指令控制，要求模型根据自然语言指令生成特定风格的语音；3) 角色扮演，要求模型模拟特定角色的说话风格；4) 隐式共情，要求模型在语音中体现出特定的情感。LALM评判器框架包含三个评估维度：文本忠实度（输出是否符合指令的语义）、风格一致性（输出是否符合指令的风格要求）和自然度（输出听起来是否自然流畅）。

**关键创新**：论文的关键创新在于：1) 提出了VSA任务，填补了SLM研究中对语音风格控制关注不足的空白；2) 构建了VStyle基准，为VSA任务提供了一个标准化的评测平台；3) 引入了LALM评判器框架，提供了一种客观、可重复的评估方法。

**关键设计**：VStyle基准包含双语（中文和英文）数据，涵盖多种语音风格和指令类型。LALM评判器框架使用大型音频语言模型作为评估器，通过训练使其能够准确评估文本忠实度、风格一致性和自然度。具体的损失函数和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，现有的商业系统和开源SLM在VStyle基准上表现出明显的局限性，尤其是在风格一致性方面。这验证了VStyle基准的挑战性和价值，并为未来的研究指明了方向。具体的性能数据和提升幅度未在摘要中详细说明，属于未知信息。

## 🎯 应用场景

该研究成果可应用于智能助手、语音合成、游戏角色配音等领域。通过提升语音风格迁移能力，可以使人机交互更加自然、个性化，增强用户体验。未来，该研究有望推动口语语言模型在情感表达、角色扮演等方面的应用。

## 📄 摘要（原文）

> Spoken language models (SLMs) have emerged as a unified paradigm for speech understanding and generation, enabling natural human machine interaction. However, while most progress has focused on semantic accuracy and instruction following, the ability of SLMs to adapt their speaking style based on spoken instructions has received limited attention. We introduce Voice Style Adaptation (VSA), a new task that examines whether SLMs can modify their speaking style, such as timbre, prosody, or persona following natural language spoken commands. To study this task, we present VStyle, a bilingual (Chinese & English) benchmark covering four categories of speech generation: acoustic attributes, natural language instruction, role play, and implicit empathy. We also introduce the Large Audio Language Model as a Judge (LALM as a Judge) framework, which progressively evaluates outputs along textual faithfulness, style adherence, and naturalness, ensuring reproducible and objective assessment. Experiments on commercial systems and open source SLMs demonstrate that current models face clear limitations in controllable style adaptation, highlighting both the novelty and challenge of this task. By releasing VStyle and its evaluation toolkit, we aim to provide the community with a foundation for advancing human centered spoken interaction. The dataset and code are publicly available at \href{https://junzhan2000.github.io/VStyle.github.io/}{project's homepage}.

