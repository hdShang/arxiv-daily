---
layout: default
title: Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting
---

# Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14115" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14115v1</a>
  <a href="https://arxiv.org/pdf/2512.14115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14115v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14115v1', 'Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ramesh Gundluru, Shubham Gupta, Sri Rama Murty K

**分类**: cs.SD, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出联合多模态对比学习框架，提升语音检索任务的鲁棒性与效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音检索` `对比学习` `多模态学习` `声学词嵌入` `语音术语检测`

## 📋 核心要点

1. 现有声学词嵌入（AWE）方法在语音检索任务中存在单模态监督和优化脱节等问题。
2. 论文提出联合多模态对比学习框架，通过音频-文本和音频-音频对比学习，统一优化嵌入空间。
3. 实验表明，该方法在词语区分任务上超越现有基线，并能灵活应用于语音术语检测和关键词检索。

## 📝 摘要（中文）

本文提出了一种联合多模态对比学习框架，旨在提升语音检索任务（如语音术语检测STD和关键词检索KWS）的性能。现有方法存在单模态监督、音频-音频和音频-文本对齐的独立优化以及需要任务特定模型等局限性。为了解决这些问题，该框架在共享嵌入空间中统一了声学和跨模态监督，同时优化了：(i) 受CLAP损失启发的音频-文本对比学习，以对齐音频和文本表示；(ii) 通过深度词语区分(DWD)损失实现的音频-音频对比学习，以增强类内紧凑性和类间分离性。实验结果表明，该方法在词语区分任务上优于现有的AWE基线，并能灵活支持STD和KWS。据我们所知，这是同类方法中的首个综合性方案。

## 🔬 方法详解

**问题定义**：论文旨在解决语音术语检测（STD）和关键词检索（KWS）任务中，现有声学词嵌入（AWE）方法的局限性。这些局限性包括：仅依赖单模态监督信号，音频-音频和音频-文本的对齐过程是独立优化的，以及需要针对特定任务训练模型。这些问题导致模型泛化能力不足，且训练效率较低。

**核心思路**：论文的核心思路是利用联合多模态对比学习，将音频和文本信息融合到一个共享的嵌入空间中。通过同时优化音频-文本和音频-音频的对比损失，模型能够学习到更鲁棒、更具区分性的语音表示。这种方法旨在克服单模态监督的不足，并实现跨模态信息的有效对齐。

**技术框架**：整体框架包含两个主要的对比学习模块：音频-文本对比学习和音频-音频对比学习。音频-文本对比学习模块使用类似于CLAP的损失函数，将音频和文本嵌入拉近，从而学习跨模态的对齐关系。音频-音频对比学习模块使用深度词语区分（DWD）损失，增强同一词语的不同音频样本之间的相似性，并增大不同词语之间的距离。这两个模块共同作用，优化共享的嵌入空间。

**关键创新**：该方法的主要创新在于联合多模态对比学习框架，它同时利用音频-文本和音频-音频信息进行监督，从而学习到更鲁棒的语音表示。与现有方法相比，该框架能够克服单模态监督的局限性，并实现跨模态信息的有效融合。此外，该框架具有通用性，可以灵活应用于不同的语音检索任务，而无需针对特定任务进行模型调整。

**关键设计**：音频-文本对比学习模块采用InfoNCE损失，鼓励音频嵌入与其对应的文本嵌入之间的相似性，同时抑制与其他文本嵌入的相似性。音频-音频对比学习模块采用DWD损失，通过最小化类内距离和最大化类间距离，增强词语的区分性。具体的网络结构和参数设置（如嵌入维度、损失函数的权重等）需要根据具体任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14115v1/figures/CLAP_for_STD.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14115v1/figures/tsne_word_embeddings.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14115v1/figures/oov_Scores_cosine.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出的方法在词语区分任务上取得了显著的性能提升，超越了现有的AWE基线。具体的性能数据和对比基线在论文中进行了详细的展示。实验结果表明，该方法能够有效地学习到鲁棒的语音表示，并能灵活应用于不同的语音检索任务。

## 🎯 应用场景

该研究成果可广泛应用于语音搜索、语音助手、智能客服等领域。通过提升语音检索的准确性和效率，可以改善用户体验，提高信息检索的效率。未来，该技术有望应用于更复杂的语音理解任务，例如语音摘要、语音翻译等。

## 📄 摘要（原文）

> Acoustic Word Embeddings (AWEs) improve the efficiency of speech retrieval tasks such as Spoken Term Detection (STD) and Keyword Spotting (KWS). However, existing approaches suffer from limitations, including unimodal supervision, disjoint optimization of audio-audio and audio-text alignment, and the need for task-specific models. To address these shortcomings, we propose a joint multimodal contrastive learning framework that unifies both acoustic and cross-modal supervision in a shared embedding space. Our approach simultaneously optimizes: (i) audio-text contrastive learning, inspired by the CLAP loss, to align audio and text representations and (ii) audio-audio contrastive learning, via Deep Word Discrimination (DWD) loss, to enhance intra-class compactness and inter-class separation. The proposed method outperforms existing AWE baselines on word discrimination task while flexibly supporting both STD and KWS. To our knowledge, this is the first comprehensive approach of its kind.

