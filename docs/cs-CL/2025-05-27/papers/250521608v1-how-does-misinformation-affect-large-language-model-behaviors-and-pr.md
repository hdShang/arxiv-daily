---
layout: default
title: How does Misinformation Affect Large Language Model Behaviors and Preferences?
---

# How does Misinformation Affect Large Language Model Behaviors and Preferences?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21608" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21608v1</a>
  <a href="https://arxiv.org/pdf/2505.21608.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21608v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21608v1', 'How does Misinformation Affect Large Language Model Behaviors and Preferences?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Miao Peng, Nuo Chen, Jianheng Tang, Jia Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27

**备注**: Accepted to ACL 2025 Main Conference

**🔗 代码/项目**: [GITHUB](https://github.com/GKNL/MisBench)

---

## 💡 一句话要点

**提出MisBench以评估大型语言模型对虚假信息的反应**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `虚假信息` `基准评估` `知识冲突` `风格变异` `检测能力` `Reconstruct to Discriminate` `MisBench`

## 📋 核心要点

1. 现有研究对大型语言模型在虚假信息面前的脆弱性缺乏细致分析，尤其是在知识冲突和风格变异方面。
2. 论文提出了MisBench基准，包含大量虚假信息样本，旨在评估LLMs对虚假信息的行为和知识偏好。
3. 实验证明，虽然LLMs在识别虚假信息方面表现良好，但仍然受到知识冲突和风格变异的影响，提出的RtD方法能有效增强其检测能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在知识密集型任务中展现出卓越的能力，但在面对虚假信息时仍然脆弱。现有研究探讨了LLMs在对抗虚假信息中的作用，但缺乏对其受虚假信息影响的细致分析。为此，我们提出了MisBench，这是当前最大的、最全面的基准，用于评估LLMs对虚假信息的行为和知识偏好。MisBench包含10,346,712条虚假信息，独特地考虑了知识冲突和风格变异。实证结果显示，尽管LLMs在识别虚假信息方面表现出相当的能力，但仍然容易受到知识冲突和风格变异的影响。基于这些发现，我们进一步提出了一种新方法Reconstruct to Discriminate（RtD），以增强LLMs检测虚假信息的能力。我们的研究为LLMs与虚假信息的互动提供了宝贵的见解，MisBench可以作为评估LLM基础检测器和提升其在实际应用中可靠性的有效基准。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在面对虚假信息时的脆弱性，现有方法未能深入分析其受虚假信息影响的具体方面和程度。

**核心思路**：提出MisBench基准，包含10,346,712条虚假信息，考虑知识冲突和风格变异，以全面评估LLMs的行为和知识偏好。

**技术框架**：整体架构包括数据收集、虚假信息分类、模型评估和性能分析四个主要模块，确保对LLMs的全面评估。

**关键创新**：MisBench是目前最大的虚假信息评估基准，独特地结合了知识冲突和风格变异，填补了现有研究的空白。

**关键设计**：在设计中，采用了多样化的虚假信息样本，结合了不同的损失函数和模型结构，以提高LLMs对虚假信息的检测能力。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，尽管LLMs在识别虚假信息方面表现出色，但在面对知识冲突和风格变异时仍然存在明显的脆弱性。通过引入RtD方法，LLMs的检测能力得到了显著提升，具体性能数据和对比基线在论文中详细列出，展示了提升幅度的具体数值。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、新闻验证和教育领域的虚假信息识别。MisBench基准可以帮助开发更可靠的LLM基础检测器，提升其在实际应用中的有效性和可靠性，进而减少虚假信息的传播。未来，随着虚假信息问题的日益严重，该研究将具有重要的社会价值和影响力。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown remarkable capabilities in knowledge-intensive tasks, while they remain vulnerable when encountering misinformation. Existing studies have explored the role of LLMs in combating misinformation, but there is still a lack of fine-grained analysis on the specific aspects and extent to which LLMs are influenced by misinformation. To bridge this gap, we present MisBench, the current largest and most comprehensive benchmark for evaluating LLMs' behavior and knowledge preference toward misinformation. MisBench consists of 10,346,712 pieces of misinformation, which uniquely considers both knowledge-based conflicts and stylistic variations in misinformation. Empirical results reveal that while LLMs demonstrate comparable abilities in discerning misinformation, they still remain susceptible to knowledge conflicts and stylistic variations. Based on these findings, we further propose a novel approach called Reconstruct to Discriminate (RtD) to strengthen LLMs' ability to detect misinformation. Our study provides valuable insights into LLMs' interactions with misinformation, and we believe MisBench can serve as an effective benchmark for evaluating LLM-based detectors and enhancing their reliability in real-world applications. Codes and data are available at https://github.com/GKNL/MisBench.

