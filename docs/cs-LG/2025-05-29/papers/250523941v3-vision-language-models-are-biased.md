---
layout: default
title: Vision Language Models are Biased
---

# Vision Language Models are Biased

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23941" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23941v3</a>
  <a href="https://arxiv.org/pdf/2505.23941.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23941v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23941v3', 'Vision Language Models are Biased')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: An Vo, Khai-Nguyen Nguyen, Mohammad Reza Taesiri, Vy Tuong Dang, Anh Totti Nguyen, Daeyoung Kim

**分类**: cs.LG, cs.CV

**发布日期**: 2025-05-29 (更新: 2025-11-30)

**备注**: Code and qualitative examples are available at: vlmsarebiased.github.io

---

## 💡 一句话要点

**揭示视觉语言模型的偏见及其对识别准确性的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `模型偏见` `计数任务` `图像处理` `推理分析`

## 📋 核心要点

1. 现有的视觉语言模型在处理标准视觉任务时，容易受到先前知识的影响，导致输出偏见和不准确。
2. 本研究通过去除图像背景和分析推理模式，探讨了如何提高视觉语言模型在计数和识别任务中的准确性。
3. 实验结果显示，去除背景后准确率提升了21.09个百分点，且思考标记的使用对准确率有显著影响。

## 📝 摘要（中文）

大型语言模型（LLMs）从互联网记忆了大量先前知识，这有助于下游任务，但也可能导致输出偏向错误或有偏见的答案。本研究测试了关于流行主题的知识如何影响视觉语言模型（VLMs）在计数和识别等标准视觉任务上的准确性。结果表明，最先进的VLMs存在显著偏见，计数准确率在七个不同领域中平均仅为17.05%。去除图像背景几乎使准确率翻倍，显示上下文视觉线索触发了这些偏见反应。进一步分析表明，VLMs的计数准确率随着思考标记的增加而上升，达到约40%，但在过度推理后下降。我们的工作展示了VLMs的一个有趣失败模式，并提出了一种人类监督的自动化框架来测试VLM的偏见。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉语言模型在计数和识别任务中存在的偏见问题，现有方法在处理流行主题时表现出显著的准确性下降。

**核心思路**：通过去除图像背景和分析推理过程，探索如何减少模型输出的偏见，提高其在视觉任务中的表现。

**技术框架**：研究采用了一个自动化框架，首先进行图像背景去除，然后通过思考标记分析模型的推理过程，最终评估模型的准确性。

**关键创新**：提出了一种新的评估框架，能够系统地测试视觉语言模型的偏见，并揭示其在特定任务中的失败模式。

**关键设计**：在实验中，去除背景的处理显著提高了模型的计数准确率，此外，思考标记的数量与准确率之间存在非线性关系，初期提升后出现下降。

## 📊 实验亮点

实验结果显示，去除图像背景后，视觉语言模型的计数准确率从17.05%提升至38.14%，提升幅度达21.09个百分点。此外，模型在使用思考标记时，准确率初期上升至约40%，但在过度推理后出现下降，揭示了模型推理过程中的复杂性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、人工智能助手和自动化内容生成等。通过识别和减少模型偏见，可以提升这些系统在实际应用中的可靠性和准确性，进而增强用户体验和信任度。未来，该研究可能推动更公平和透明的AI系统设计。

## 📄 摘要（原文）

> Large language models (LLMs) memorize a vast amount of prior knowledge from the Internet that helps them on downstream tasks but also may notoriously sway their outputs towards wrong or biased answers. In this work, we test how the knowledge about popular subjects hurt the accuracy of vision language models (VLMs) on standard, objective visual tasks of counting and identification. We find that state-of-the-art VLMs are strongly biased (e.g., unable to recognize the 4th stripe has been added to a 3-stripe Adidas logo) scoring an average of 17.05% accuracy in counting (e.g., counting stripes in an Adidas-like logo) across 7 diverse domains from animals, logos, chess, board games, optical illusions, to patterned grids. Removing image backgrounds nearly doubles accuracy (21.09 percentage points), revealing that contextual visual cues trigger these biased responses. Further analysis of VLMs' reasoning patterns shows that counting accuracy initially rises with thinking tokens, reaching ~40%, before declining with excessive reasoning. Our work presents an interesting failure mode in VLMs and a human-supervised automated framework for testing VLM biases. Code and data are available at: vlmsarebiased.github.io.

