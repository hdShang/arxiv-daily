---
layout: default
title: "ReasonCD: A Multimodal Reasoning Large Model for Implicit Change-of-Interest Semantic Mining"
---

# ReasonCD: A Multimodal Reasoning Large Model for Implicit Change-of-Interest Semantic Mining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19354" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19354v1</a>
  <a href="https://arxiv.org/pdf/2512.19354.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19354v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19354v1', 'ReasonCD: A Multimodal Reasoning Large Model for Implicit Change-of-Interest Semantic Mining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyang Huang, Xiao Yu, Yi Zhang, Decheng Wang, Hang Ruan

**分类**: cs.CV

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**ReasonCD：提出多模态推理大模型，用于遥感图像隐式兴趣变更语义挖掘**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像变化检测` `多模态推理` `大语言模型` `隐式语义挖掘` `预训练模型`

## 📋 核心要点

1. 现有遥感变化检测方法依赖显式文本描述，无法处理隐式兴趣变更语义，导致性能下降。
2. ReasonCD模型利用预训练大语言模型的推理能力，挖掘用户隐式意图，指导变化检测。
3. 实验表明，ReasonCD在BCDD数据集上F1值达92.1%，并能解释推理过程辅助决策。

## 📝 摘要（中文）

遥感图像变化检测是遥感智能解译中的一项基础任务，其核心目标是识别感兴趣的变化区域（CRoI）内的变化。目前的多模态大模型编码了丰富的人类语义知识，可用于指导遥感变化检测等任务。然而，现有方法在利用语义指导检测用户的CRoI时，过度依赖于CRoI的显式文本描述，导致在面对隐式CRoI文本描述时，性能几乎完全失效。本文提出了一种名为ReasonCD的多模态推理变化检测模型，该模型能够挖掘用户的隐式任务意图。该模型利用预训练大语言模型的强大推理能力来挖掘用户的隐式任务意图，并根据这些意图获得不同的变化检测结果。在公共数据集上的实验表明，该模型实现了出色的变化检测性能，在BCDD数据集上的F1得分为92.1%。此外，为了验证其卓越的推理功能，本文基于SECOND数据集标注了一个推理数据子集。实验结果表明，该模型不仅擅长基于基本推理的变化检测任务，还可以解释推理过程，以辅助人类决策。

## 🔬 方法详解

**问题定义**：遥感图像变化检测旨在识别图像中发生变化的区域。现有方法依赖于对感兴趣变化区域（CRoI）的显式文本描述，当用户提供的是隐式或模糊的描述时，这些方法无法准确理解用户的意图，导致检测性能显著下降。这种对显式信息的过度依赖是现有方法的痛点。

**核心思路**：ReasonCD的核心思路是利用预训练大语言模型（LLM）强大的推理能力，从用户的隐式文本描述中挖掘出其真实的意图。通过理解用户意图，模型可以更准确地识别出用户真正感兴趣的变化区域，从而提高变化检测的准确性。这种方法避免了对显式文本描述的过度依赖。

**技术框架**：ReasonCD模型主要包含以下几个关键模块：1) 多模态输入编码器：用于提取遥感图像和文本描述的特征。2) 大语言模型推理模块：利用预训练的LLM，根据图像特征和文本描述，推理出用户的隐式意图。3) 变化检测模块：根据LLM推理出的用户意图，对图像进行变化检测，生成变化区域的掩码。整体流程是先进行多模态特征提取，然后利用LLM进行意图推理，最后根据推理结果进行变化检测。

**关键创新**：ReasonCD的关键创新在于将预训练大语言模型的推理能力引入到遥感图像变化检测任务中。与现有方法不同，ReasonCD能够处理隐式文本描述，挖掘用户的真实意图，从而实现更准确的变化检测。这种基于推理的方法是与现有方法最本质的区别。

**关键设计**：ReasonCD的关键设计包括：1) 使用预训练的LLM作为推理模块，充分利用其强大的语义理解和推理能力。2) 设计了合适的提示工程（Prompt Engineering），引导LLM进行意图推理。3) 针对遥感图像变化检测任务，对LLM进行了微调，以提高其在该任务上的性能。损失函数方面，可能采用了交叉熵损失或Dice损失等，以优化变化检测的准确性。具体的网络结构细节和参数设置需要在论文中进一步查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19354v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19354v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19354v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ReasonCD在BCDD数据集上取得了92.1%的F1分数，证明了其出色的变化检测性能。更重要的是，该模型在基于SECOND数据集构建的推理数据集上表现出色，不仅能完成推理任务，还能解释推理过程，为人类决策提供依据。这表明ReasonCD具有强大的推理能力和实用价值。

## 🎯 应用场景

ReasonCD可应用于灾害评估、城市规划、环境监测等领域。通过理解用户的隐式需求，该模型能够更准确地识别出感兴趣的变化区域，为决策者提供更可靠的信息支持。未来，该模型有望应用于更广泛的遥感图像分析任务，例如目标检测、图像分割等，提升遥感智能解译的自动化水平。

## 📄 摘要（原文）

> Remote sensing image change detection is one of the fundamental tasks in remote sensing intelligent interpretation. Its core objective is to identify changes within change regions of interest (CRoI). Current multimodal large models encode rich human semantic knowledge, which is utilized for guidance in tasks such as remote sensing change detection. However, existing methods that use semantic guidance for detecting users' CRoI overly rely on explicit textual descriptions of CRoI, leading to the problem of near-complete performance failure when presented with implicit CRoI textual descriptions. This paper proposes a multimodal reasoning change detection model named ReasonCD, capable of mining users' implicit task intent. The model leverages the powerful reasoning capabilities of pre-trained large language models to mine users' implicit task intents and subsequently obtains different change detection results based on these intents. Experiments on public datasets demonstrate that the model achieves excellent change detection performance, with an F1 score of 92.1\% on the BCDD dataset. Furthermore, to validate its superior reasoning functionality, this paper annotates a subset of reasoning data based on the SECOND dataset. Experimental results show that the model not only excels at basic reasoning-based change detection tasks but can also explain the reasoning process to aid human decision-making.

