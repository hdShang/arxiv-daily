---
layout: default
title: "ReviewScore: Misinformed Peer Review Detection with Large Language Models"
---

# ReviewScore: Misinformed Peer Review Detection with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21679" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21679v1</a>
  <a href="https://arxiv.org/pdf/2509.21679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21679v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21679v1', 'ReviewScore: Misinformed Peer Review Detection with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyun Ryu, Doohyuk Jang, Hyemin S. Lee, Joonhyun Jeong, Gyeongman Kim, Donghyeon Cho, Gyouk Chu, Minyeong Hwang, Hyeongwon Jang, Changhun Kim, Haechan Kim, Jina Kim, Joowon Kim, Yoonjeon Kim, Kwanhyung Lee, Chanjae Park, Heecheol Yun, Gregor Betz, Eunho Yang

**分类**: cs.CL

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**提出ReviewScore以检测同行评审中的错误信息，提升评审质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `同行评审` `错误信息检测` `大型语言模型` `自然语言处理` `评审质量评估`

## 📋 核心要点

1. AI会议评审质量下降，现有方法难以有效识别低质量评审中的错误信息。
2. 提出ReviewScore，通过识别评审中的错误前提和已解答问题来评估评审质量。
3. 构建ReviewScore数据集，实验表明LLM在评估前提真实性方面表现出与人类评审员的中等一致性。

## 📝 摘要（中文）

同行评审是学术研究的基石，但随着AI会议投稿数量的爆炸式增长，评审质量正在下降。为了可靠地检测低质量的评审，我们将错误信息评审点定义为评审中的“弱点”（包含不正确的前提）或“问题”（论文中已解答）。我们验证了15.2%的弱点和26.4%的问题包含错误信息，并引入ReviewScore来指示评审点是否包含错误信息。为了评估弱点中每个前提的真实性，我们提出了一个自动引擎，可以从弱点中重建每个显式和隐式前提。我们构建了一个人工专家标注的ReviewScore数据集，以检查LLM自动评估ReviewScore的能力。然后，我们使用八个当前最先进的LLM测量了人类与模型在ReviewScore上的一致性，并验证了中等程度的一致性。我们还证明了评估前提层面的真实性比评估弱点层面的真实性显示出更高的一致性。深入的差异分析进一步支持了完全自动化ReviewScore评估的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决AI学术会议中同行评审质量下降的问题，具体而言，是识别评审报告中包含错误信息的部分，包括基于不正确前提的“弱点”和论文中已解答的“问题”。现有方法难以有效识别这些错误信息，导致评审质量参差不齐。

**核心思路**：论文的核心思路是将评审报告中的“弱点”分解为更细粒度的前提，并评估这些前提的真实性。同时，检测评审提出的“问题”是否已经在论文中得到解答。通过量化评审报告中错误信息的比例，从而评估评审质量。

**技术框架**：论文提出了一个自动化的ReviewScore评估引擎，主要包含以下几个阶段：1) 从评审报告的“弱点”中提取显式和隐式前提；2) 使用LLM评估每个前提的真实性；3) 检测评审提出的“问题”是否在论文中已解答；4) 根据错误信息的比例计算ReviewScore。

**关键创新**：论文的关键创新在于提出了ReviewScore的概念，并设计了一个自动化的评估引擎，能够从细粒度的前提层面评估评审报告的质量。与以往关注整体评审质量的方法不同，该方法能够更精确地定位评审报告中的错误信息。

**关键设计**：论文构建了一个人工标注的ReviewScore数据集，用于训练和评估LLM。在评估前提真实性时，使用了多个最先进的LLM，并比较了它们与人类评审员的一致性。论文还分析了人类评审员和LLM之间的差异，为进一步改进自动化评估引擎提供了指导。

## 📊 实验亮点

实验结果表明，15.2%的评审“弱点”和26.4%的评审“问题”包含错误信息。使用LLM评估前提层面的真实性，与人类评审员的一致性达到中等水平，显著高于评估弱点层面的真实性。这些结果验证了ReviewScore的可行性，并为自动化评审质量评估提供了有力的支持。

## 🎯 应用场景

该研究成果可应用于自动化评审质量评估系统，帮助会议组织者筛选高质量的评审报告，提高评审效率和公平性。此外，该方法还可以用于评审员培训，帮助评审员避免在评审报告中出现错误信息，提升整体评审质量。未来，该技术有望扩展到其他领域的同行评审，例如期刊论文评审。

## 📄 摘要（原文）

> Peer review serves as a backbone of academic research, but in most AI conferences, the review quality is degrading as the number of submissions explodes. To reliably detect low-quality reviews, we define misinformed review points as either "weaknesses" in a review that contain incorrect premises, or "questions" in a review that can be already answered by the paper. We verify that 15.2% of weaknesses and 26.4% of questions are misinformed and introduce ReviewScore indicating if a review point is misinformed. To evaluate the factuality of each premise of weaknesses, we propose an automated engine that reconstructs every explicit and implicit premise from a weakness. We build a human expert-annotated ReviewScore dataset to check the ability of LLMs to automate ReviewScore evaluation. Then, we measure human-model agreements on ReviewScore using eight current state-of-the-art LLMs and verify moderate agreements. We also prove that evaluating premise-level factuality shows significantly higher agreements than evaluating weakness-level factuality. A thorough disagreement analysis further supports a potential of fully automated ReviewScore evaluation.

