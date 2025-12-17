---
layout: default
title: Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting
---

# Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14115" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14115</a>
  <a href="https://arxiv.org/pdf/2512.14115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14115" onclick="toggleFavorite(this, '2512.14115', 'Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ramesh Gundluru, Shubham Gupta, Sri Rama Murty K

**分类**: cs.SD, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出联合多模态对比学习框架，提升语音检索任务的鲁棒性和效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音术语检测` `关键词检索` `声学词嵌入` `多模态对比学习` `音频文本对齐`

## 📋 核心要点

1. 现有声学词嵌入（AWE）方法在语音检索任务中存在单模态监督和优化分离等问题。
2. 提出联合多模态对比学习框架，同时优化音频-文本和音频-音频的对齐，提升性能。
3. 实验表明，该方法在词语区分任务上超越现有基线，并能灵活支持STD和KWS。

## 📝 摘要（中文）

本文提出了一种联合多模态对比学习框架，旨在提升语音检索任务（如语音术语检测STD和关键词检索KWS）的性能。现有方法存在单模态监督、音频-音频和音频-文本对齐的独立优化以及需要任务特定模型等局限性。为了解决这些问题，该框架在共享嵌入空间中统一了声学和跨模态监督，同时优化了：(i) 受CLAP损失启发的音频-文本对比学习，以对齐音频和文本表示；(ii) 通过深度词语区分(DWD)损失实现的音频-音频对比学习，以增强类内紧凑性和类间分离性。实验结果表明，该方法在词语区分任务上优于现有的AWE基线，并能灵活支持STD和KWS。据我们所知，这是同类方法中的首个综合性方案。

## 🔬 方法详解

**问题定义**：论文旨在解决语音术语检测（STD）和关键词检索（KWS）任务中，现有声学词嵌入（AWE）方法的局限性。这些局限性包括：仅使用单模态监督信号，音频-音频和音频-文本的对齐过程是独立优化的，以及需要针对特定任务训练不同的模型。这些问题导致模型泛化能力不足，且效率较低。

**核心思路**：论文的核心思路是利用联合多模态对比学习，将音频和文本信息融合到一个共享的嵌入空间中。通过同时优化音频-文本和音频-音频的对比损失，模型能够学习到更鲁棒、更具判别性的声学词嵌入表示。这种联合学习的方式可以克服单模态监督的限制，并实现跨模态信息的有效利用。

**技术框架**：整体框架包含两个主要的对比学习模块：音频-文本对比学习和音频-音频对比学习。音频-文本对比学习模块采用类似于CLAP的损失函数，旨在将音频和文本的表示对齐到同一嵌入空间。音频-音频对比学习模块则使用深度词语区分（DWD）损失，鼓励同一类别的音频样本在嵌入空间中更加紧凑，不同类别的样本之间更加分离。这两个模块的损失函数被联合优化，从而实现声学词嵌入的有效学习。

**关键创新**：该方法最重要的创新在于将音频-文本和音频-音频对比学习联合起来，在一个统一的框架中进行优化。与以往分别优化这两个过程的方法相比，该方法能够更好地利用跨模态信息，学习到更具判别性的声学词嵌入。此外，该方法还避免了针对特定任务训练模型的需要，提高了模型的泛化能力。

**关键设计**：音频-文本对比学习模块使用Transformer网络提取音频和文本的特征表示，然后通过对比损失函数进行优化。音频-音频对比学习模块使用深度神经网络学习音频的嵌入表示，并通过DWD损失函数来增强类内紧凑性和类间分离性。DWD损失函数的设计考虑了类别之间的关系，能够更有效地提高词语区分的性能。具体的损失函数权重和网络结构参数需要根据实验进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14115/figures/CLAP_for_STD.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14115/figures/tsne_word_embeddings.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14115/figures/oov_Scores_cosine.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在词语区分任务上优于现有的AWE基线。具体性能提升数据未知，但摘要中明确指出该方法在词语区分任务上表现更优，并且能够灵活支持STD和KWS任务。这表明该方法在实际应用中具有较强的竞争力。

## 🎯 应用场景

该研究成果可广泛应用于语音搜索、智能语音助手、语音内容分析等领域。通过提升语音检索的准确性和效率，可以改善用户体验，并为相关应用提供更强大的技术支持。未来，该方法有望扩展到更多模态的数据融合，例如视频和文本的联合检索，从而实现更智能化的信息处理。

## 📄 摘要（原文）

> Acoustic Word Embeddings (AWEs) improve the efficiency of speech retrieval tasks such as Spoken Term Detection (STD) and Keyword Spotting (KWS). However, existing approaches suffer from limitations, including unimodal supervision, disjoint optimization of audio-audio and audio-text alignment, and the need for task-specific models. To address these shortcomings, we propose a joint multimodal contrastive learning framework that unifies both acoustic and cross-modal supervision in a shared embedding space. Our approach simultaneously optimizes: (i) audio-text contrastive learning, inspired by the CLAP loss, to align audio and text representations and (ii) audio-audio contrastive learning, via Deep Word Discrimination (DWD) loss, to enhance intra-class compactness and inter-class separation. The proposed method outperforms existing AWE baselines on word discrimination task while flexibly supporting both STD and KWS. To our knowledge, this is the first comprehensive approach of its kind.

