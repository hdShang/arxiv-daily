---
layout: default
title: "OS-W2S: An Automatic Labeling Engine for Language-Guided Open-Set Aerial Object Detection"
---

# OS-W2S: An Automatic Labeling Engine for Language-Guided Open-Set Aerial Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03334" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03334v2</a>
  <a href="https://arxiv.org/pdf/2505.03334.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03334v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03334v2', 'OS-W2S: An Automatic Labeling Engine for Language-Guided Open-Set Aerial Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guoting Wei, Yu Liu, Xia Yuan, Xizhe Xue, Linlin Guo, Yifan Yang, Chunxia Zhao, Zongwen Bai, Haokui Zhang, Rong Xiao

**分类**: cs.CV, cs.DB

**发布日期**: 2025-05-06 (更新: 2025-09-26)

**🔗 代码/项目**: [GITHUB](https://github.com/GT-Wei/MI-OAD)

---

## 💡 一句话要点

**提出OS-W2S引擎以解决语言引导的开放集空中物体检测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放集检测` `语言引导` `空中物体检测` `数据集构建` `深度学习` `视觉-语言模型` `自动注释` `遥感技术`

## 📋 核心要点

1. 现有语言引导的开放集空中物体检测方法主要集中在词汇级别，无法满足细粒度检测需求。
2. 本文提出了OS-W2S标签引擎，通过构建多层次的语言引导数据集，解决了现有数据集的局限性。
3. 在MI-OAD数据集上进行的实验显示，使用该数据集训练的模型在多个任务上显著提升了检测性能。

## 📝 摘要（中文）

近年来，语言引导的开放集空中物体检测因其更好地满足实际应用需求而受到广泛关注。然而，由于数据集的限制，现有方法主要集中在词汇级别的描述，无法满足细粒度开放世界检测的需求。为了解决这一限制，本文构建了一个大规模的语言引导开放集空中检测数据集，涵盖了从单词到短语，再到句子的三种语言引导层次。基于开源的大型视觉-语言模型，结合基于图像操作的预处理和基于BERT的后处理，提出了OS-W2S标签引擎，能够自动处理空中图像的多样场景注释。通过该引擎，我们扩展了现有的空中检测数据集，构建了一个新的基准数据集MI-OAD，包含163,023张图像和200万对图像-文本描述，约为现有数据集的40倍。实验结果表明，MI-OAD在语言引导的开放集空中检测任务中显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决语言引导的开放集空中物体检测中，现有方法在数据集规模和描述细粒度上的不足。现有方法主要依赖于词汇级别的描述，无法有效支持复杂场景的检测需求。

**核心思路**：论文提出了OS-W2S标签引擎，通过构建一个包含丰富文本注释的大规模数据集MI-OAD，提供从单词到句子的多层次语言引导，以增强模型的检测能力。

**技术框架**：整体架构包括数据集构建、标签引擎设计和模型训练三个主要模块。数据集构建阶段使用图像操作进行预处理，标签引擎则利用BERT进行后处理，最终生成高质量的图像-文本对。

**关键创新**：最重要的创新在于构建了一个包含163,023张图像和200万对图像-文本描述的MI-OAD数据集，显著扩大了现有数据集的规模，并提供了多层次的语言引导。

**关键设计**：在标签引擎中，采用了图像操作与BERT结合的方式进行注释，确保了生成的文本描述的准确性和多样性，同时在训练过程中优化了损失函数以提升模型的检测性能。

## 📊 实验亮点

在语言引导的开放集空中检测任务中，使用MI-OAD数据集训练的模型在AP$_{50}$上提升了31.1，Recall@10提升了34.7，展示了该数据集的有效性和OS-W2S注释的高质量。此外，MI-OAD在多个开放词汇空中检测和遥感视觉定位基准上也取得了最先进的性能，验证了其广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机监测、环境保护、城市规划等，能够为复杂场景下的物体检测提供更为精准的支持。通过丰富的文本注释，未来可进一步推动智能监控和自动化决策系统的发展，提升相关领域的工作效率和准确性。

## 📄 摘要（原文）

> In recent years, language-guided open-set aerial object detection has gained significant attention due to its better alignment with real-world application needs. However, due to limited datasets, most existing language-guided methods primarily focus on vocabulary-level descriptions, which fail to meet the demands of fine-grained open-world detection. To address this limitation, we propose constructing a large-scale language-guided open-set aerial detection dataset, encompassing three levels of language guidance: from words to phrases, and ultimately to sentences. Centered around an open-source large vision-language model and integrating image-operation-based preprocessing with BERT-based postprocessing, we present the OS-W2S Label Engine, an automatic annotation pipeline capable of handling diverse scene annotations for aerial images. Using this label engine, we expand existing aerial detection datasets with rich textual annotations and construct a novel benchmark dataset, called MI-OAD, addressing the limitations of current remote sensing grounding data and enabling effective language-guided open-set aerial detection. Specifically, MI-OAD contains 163,023 images and 2 million image-caption pairs, approximately 40 times larger than comparable datasets. To demonstrate the effectiveness and quality of MI-OAD, we evaluate three representative tasks. On language-guided open-set aerial detection, training on MI-OAD lifts Grounding DINO by +31.1 AP$_{50}$ and +34.7 Recall@10 with sentence-level inputs under zero-shot transfer. Moreover, using MI-OAD for pre-training yields state-of-the-art performance on multiple existing open-vocabulary aerial detection and remote sensing visual grounding benchmarks, validating both the effectiveness of the dataset and the high quality of its OS-W2S annotations. More details are available at https://github.com/GT-Wei/MI-OAD.

