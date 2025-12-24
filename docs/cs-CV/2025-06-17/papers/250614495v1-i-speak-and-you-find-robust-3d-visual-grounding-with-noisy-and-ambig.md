---
layout: default
title: "I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs"
---

# I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14495" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14495v1</a>
  <a href="https://arxiv.org/pdf/2506.14495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14495v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14495v1', 'I Speak and You Find: Robust 3D Visual Grounding with Noisy and Ambiguous Speech Inputs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Qi, Lipeng Gu, Honghua Chen, Liangliang Nan, Mingqiang Wei

**分类**: cs.CV

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出SpeechRefer以解决噪声和模糊语音输入下的3D视觉定位问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉定位` `语音识别` `多模态融合` `对比学习` `鲁棒性`

## 📋 核心要点

1. 现有3D视觉定位方法依赖精确文本提示，无法有效处理噪声和模糊的语音输入。
2. 提出SpeechRefer框架，通过语音补充模块和对比补充模块增强对噪声和模糊语音的鲁棒性。
3. 在SpeechRefer和SpeechNr3D数据集上的实验表明，SpeechRefer显著提升了现有方法的性能，具有实际应用潜力。

## 📝 摘要（中文）

现有的3D视觉定位方法依赖于精确的文本提示来定位3D场景中的物体。然而，现实中的语音输入常常受到口音、背景噪音和语速变化等因素的影响，导致转录错误，从而限制了现有3D视觉定位方法的适用性。为了解决这些挑战，本文提出了SpeechRefer，一个旨在增强在噪声和模糊语音转录情况下性能的3D视觉定位框架。SpeechRefer与现有的3D视觉定位模型无缝集成，并引入了两个关键创新：语音补充模块和对比补充模块。实验结果表明，SpeechRefer显著提升了现有3D视觉定位方法的性能，展示了其在多模态系统中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D视觉定位方法在处理噪声和模糊语音输入时的局限性，尤其是由于转录错误导致的性能下降。现有方法对精确文本的依赖使其在实际应用中面临挑战。

**核心思路**：SpeechRefer框架通过引入语音补充模块和对比补充模块，减少对错误转录的依赖，增强系统在噪声环境下的鲁棒性。这样的设计使得系统能够更好地利用语音信号中的信息。

**技术框架**：SpeechRefer整体架构包括两个主要模块：语音补充模块用于捕捉声学相似性并生成补充提案分数；对比补充模块则通过对比学习对齐错误文本特征和相应的语音特征。

**关键创新**：最重要的技术创新在于引入了语音补充模块和对比补充模块，这与现有方法的本质区别在于不再单纯依赖文本转录，而是通过声学特征增强系统的鲁棒性。

**关键设计**：在设计中，语音补充模块通过分析声学相似性来生成补充分数，而对比补充模块则使用对比损失函数来确保文本和语音特征的对齐，具体的网络结构和参数设置在实验中进行了详细调优。

## 📊 实验亮点

在实验中，SpeechRefer在SpeechRefer和SpeechNr3D数据集上表现出显著的性能提升，相较于基线方法，性能提升幅度达到XX%（具体数据待补充），验证了其在处理噪声和模糊语音输入方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、增强现实和虚拟现实等多模态交互系统。通过提高系统对噪声和模糊语音的理解能力，SpeechRefer能够在实际场景中提供更为直观和自然的用户体验，推动多模态技术的发展。

## 📄 摘要（原文）

> Existing 3D visual grounding methods rely on precise text prompts to locate objects within 3D scenes. Speech, as a natural and intuitive modality, offers a promising alternative. Real-world speech inputs, however, often suffer from transcription errors due to accents, background noise, and varying speech rates, limiting the applicability of existing 3DVG methods. To address these challenges, we propose \textbf{SpeechRefer}, a novel 3DVG framework designed to enhance performance in the presence of noisy and ambiguous speech-to-text transcriptions. SpeechRefer integrates seamlessly with xisting 3DVG models and introduces two key innovations. First, the Speech Complementary Module captures acoustic similarities between phonetically related words and highlights subtle distinctions, generating complementary proposal scores from the speech signal. This reduces dependence on potentially erroneous transcriptions. Second, the Contrastive Complementary Module employs contrastive learning to align erroneous text features with corresponding speech features, ensuring robust performance even when transcription errors dominate. Extensive experiments on the SpeechRefer and peechNr3D datasets demonstrate that SpeechRefer improves the performance of existing 3DVG methods by a large margin, which highlights SpeechRefer's potential to bridge the gap between noisy speech inputs and reliable 3DVG, enabling more intuitive and practical multimodal systems.

