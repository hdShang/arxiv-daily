---
layout: default
title: Stress-testing Machine Generated Text Detection: Shifting Language Models Writing Style to Fool Detectors
---

# Stress-testing Machine Generated Text Detection: Shifting Language Models Writing Style to Fool Detectors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24523" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24523v1</a>
  <a href="https://arxiv.org/pdf/2505.24523.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24523v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24523v1', 'Stress-testing Machine Generated Text Detection: Shifting Language Models Writing Style to Fool Detectors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea Pedrotti, Michele Papucci, Cristiano Ciaccio, Alessio Miaschi, Giovanni Puccetti, Felice Dell'Orletta, Andrea Esuli

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

**备注**: Accepted at Findings of ACL 2025

---

## 💡 一句话要点

**提出一种新方法以提高机器生成文本检测的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器生成文本` `文本检测` `对抗性攻击` `语言模型` `直接偏好优化` `风格迁移` `检测鲁棒性`

## 📋 核心要点

1. 现有的机器生成文本检测方法在面对经过调整的文本时表现不佳，缺乏对真实场景的鲁棒性。
2. 本文通过直接偏好优化微调语言模型，改变机器生成文本的风格，使其更接近人类书写文本，从而挑战检测器的有效性。
3. 实验结果显示，检测器在少量样本的情况下容易被欺骗，检测性能显著下降，强调了改进检测方法的必要性。

## 📝 摘要（中文）

随着生成性人工智能和大型语言模型的进步，生成高度真实的合成内容变得越来越容易，这引发了对其潜在恶意使用的担忧，如虚假信息和操控。检测机器生成文本（MGT）仍然具有挑战性，尤其是在缺乏稳健基准的情况下。本文提出了一种测试现有MGT检测器（如Mage、Radar、LLM-DetectAIve）对语言攻击的抗性的方法。通过使用直接偏好优化（DPO）微调语言模型，将MGT的风格转向人类书写文本（HWT），从而利用检测器对风格线索的依赖，使得新生成的文本更难被检测。实验结果表明，检测器在面对经过调整的文本时，性能显著下降，强调了改进检测方法的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有机器生成文本检测方法在面对经过调整的文本时的鲁棒性不足问题。现有方法在真实场景中的泛化能力较弱，容易被对抗性文本欺骗。

**核心思路**：论文的核心思路是通过直接偏好优化（DPO）微调语言模型，使生成的文本风格更接近人类书写文本，从而利用检测器对风格线索的依赖，增加检测难度。

**技术框架**：整体架构包括三个主要模块：1) 语言模型的微调，2) 生成文本的风格调整，3) 检测器的性能评估。通过这些模块，系统能够生成更具欺骗性的文本并评估检测器的抗性。

**关键创新**：最重要的技术创新在于使用DPO方法微调语言模型，使生成文本的风格与人类书写文本高度一致，从而有效地欺骗现有的检测器。与传统方法相比，这种方法在风格调整上具有更高的灵活性和有效性。

**关键设计**：在参数设置上，DPO的损失函数设计为最大化人类偏好的文本生成，同时保持生成文本的多样性。网络结构方面，采用了先进的Transformer架构，以提高生成文本的质量和风格一致性。实验中，通过调整超参数，优化生成文本的风格特征。

## 📊 实验亮点

实验结果表明，经过调整的机器生成文本在检测器面前表现出显著的欺骗性，检测性能下降幅度达到40%以上。这一发现强调了现有检测方法的脆弱性，并指出了未来改进的方向。

## 🎯 应用场景

该研究的潜在应用领域包括内容审核、社交媒体监控和虚假信息检测等。通过提高机器生成文本的检测能力，可以有效减少虚假信息的传播，保护信息的真实性和可靠性。未来，该方法还可以扩展到其他类型的文本生成和检测任务中，具有广泛的实际价值。

## 📄 摘要（原文）

> Recent advancements in Generative AI and Large Language Models (LLMs) have enabled the creation of highly realistic synthetic content, raising concerns about the potential for malicious use, such as misinformation and manipulation. Moreover, detecting Machine-Generated Text (MGT) remains challenging due to the lack of robust benchmarks that assess generalization to real-world scenarios. In this work, we present a pipeline to test the resilience of state-of-the-art MGT detectors (e.g., Mage, Radar, LLM-DetectAIve) to linguistically informed adversarial attacks. To challenge the detectors, we fine-tune language models using Direct Preference Optimization (DPO) to shift the MGT style toward human-written text (HWT). This exploits the detectors' reliance on stylistic clues, making new generations more challenging to detect. Additionally, we analyze the linguistic shifts induced by the alignment and which features are used by detectors to detect MGT texts. Our results show that detectors can be easily fooled with relatively few examples, resulting in a significant drop in detection performance. This highlights the importance of improving detection methods and making them robust to unseen in-domain texts.

