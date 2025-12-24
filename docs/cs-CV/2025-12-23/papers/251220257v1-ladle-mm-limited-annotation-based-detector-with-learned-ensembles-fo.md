---
layout: default
title: LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation
---

# LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20257" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20257v1</a>
  <a href="https://arxiv.org/pdf/2512.20257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20257v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20257v1', 'LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniele Cardullo, Simone Teglia, Irene Amerini

**分类**: cs.CV

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出LADLE-MM，一种基于有限标注和集成学习的多模态信息检测器，适用于资源受限场景。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态信息检测` `有限标注学习` `模型集成` `模型汤` `视觉语言模型`

## 📋 核心要点

1. 现有信息检测方法依赖于计算密集型架构或需要大量标注数据，限制了其在资源受限场景下的应用。
2. LADLE-MM利用模型汤初始化，结合单模态和多模态分支，并引入BLIP嵌入作为参考空间，提升检测性能。
3. 实验表明，LADLE-MM在DGM4和VERITE数据集上均取得了竞争力的性能，且参数量更少，泛化能力更强。

## 📝 摘要（中文）

随着多媒体内容生成和操纵工具的普及，对数字媒体进行逼真的合成篡改已成为一种普遍威胁，通常涉及跨多种模态的同时操作。 近年来，此类技术越来越多地被用于歪曲重要事件的叙述并在社交媒体上传播虚假信息，从而推动了信息检测器的发展。 在通过图像-文本对传递的错误信息的背景下，已经提出了几种检测方法。 然而，这些方法通常依赖于计算密集型架构或需要大量的标注数据。 在这项工作中，我们介绍了LADLE-MM：基于有限标注的检测器，具有用于多模态错误信息的学习集成，这是一种模型汤初始化的多模态错误信息检测器，旨在在有限的标注设置和受约束的训练资源下运行。 LADLE-MM由两个单模态分支和一个第三个多模态分支组成，该分支使用从BLIP提取的附加多模态嵌入来增强图像和文本表示，作为固定的参考空间。 尽管使用的可训练参数比以前最先进的模型少60.3％，但LADLE-MM在DGM4基准测试中的二元和多标签分类任务上均实现了具有竞争力的性能，在没有grounding标注的情况下进行训练时，其性能优于现有方法。 此外，在VERITE数据集上进行评估时，LADLE-MM的性能优于当前使用涉及大型视觉-语言模型的更复杂架构的最新方法，从而证明了在开放集设置中的有效泛化能力以及对单模态偏差的强大鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决在有限标注和计算资源下，如何高效准确地检测多模态（图像-文本）信息的问题。现有方法通常需要大量的标注数据或依赖于复杂的模型架构，导致训练成本高昂，难以在资源受限的环境中应用。

**核心思路**：论文的核心思路是利用模型集成和预训练模型提供的知识，在有限的标注数据下训练出高性能的多模态信息检测器。通过模型汤初始化，可以有效地利用多个模型的优势，提高模型的泛化能力和鲁棒性。同时，引入BLIP提取的多模态嵌入作为参考空间，可以增强图像和文本表示，从而提高检测的准确性。

**技术框架**：LADLE-MM的整体架构包含三个主要分支：两个单模态分支（分别处理图像和文本）和一个多模态分支。单模态分支负责提取图像和文本的特征表示。多模态分支则将图像和文本特征与从BLIP提取的多模态嵌入进行融合，从而增强表示能力。最后，将三个分支的输出进行集成，得到最终的检测结果。

**关键创新**：LADLE-MM的关键创新在于以下几点：1) 采用了模型汤初始化，可以有效地利用多个模型的知识，提高模型的泛化能力。2) 引入了BLIP提取的多模态嵌入作为参考空间，增强了图像和文本表示，提高了检测的准确性。3) 在有限标注数据下取得了具有竞争力的性能，且参数量更少，更易于部署。

**关键设计**：LADLE-MM的关键设计包括：1) 使用预训练的图像和文本编码器作为单模态分支的初始化。2) 使用BLIP模型提取图像-文本对的多模态嵌入，并将其作为固定的参考空间。3) 使用模型汤技术对多个模型的权重进行平均，得到最终的模型。4) 损失函数包括二元交叉熵损失和多标签分类损失，用于优化模型的分类性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20257v1/img/model.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20257v1/img/unmanipulated_pair.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20257v1/img/pca.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LADLE-MM在DGM4基准测试中，使用比现有SOTA模型少60.3%的参数量，取得了具有竞争力的性能，尤其是在没有grounding标注的情况下，优于现有方法。在VERITE数据集上，LADLE-MM也超越了使用更复杂架构（包括大型视觉-语言模型）的SOTA方法，展示了其强大的泛化能力和对单模态偏差的鲁棒性。

## 🎯 应用场景

该研究成果可应用于社交媒体平台、新闻媒体等领域，用于自动检测和过滤虚假信息，维护网络信息安全。在资源受限的情况下，该方法也能有效部署，具有重要的实际应用价值。未来可进一步扩展到其他模态，如视频、音频等，构建更全面的信息检测系统。

## 📄 摘要（原文）

> With the rise of easily accessible tools for generating and manipulating multimedia content, realistic synthetic alterations to digital media have become a widespread threat, often involving manipulations across multiple modalities simultaneously. Recently, such techniques have been increasingly employed to distort narratives of important events and to spread misinformation on social media, prompting the development of misinformation detectors. In the context of misinformation conveyed through image-text pairs, several detection methods have been proposed. However, these approaches typically rely on computationally intensive architectures or require large amounts of annotated data. In this work we introduce LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation, a model-soup initialized multimodal misinformation detector designed to operate under a limited annotation setup and constrained training resources. LADLE-MM is composed of two unimodal branches and a third multimodal one that enhances image and text representations with additional multimodal embeddings extracted from BLIP, serving as fixed reference space. Despite using 60.3% fewer trainable parameters than previous state-of-the-art models, LADLE-MM achieves competitive performance on both binary and multi-label classification tasks on the DGM4 benchmark, outperforming existing methods when trained without grounding annotations. Moreover, when evaluated on the VERITE dataset, LADLE-MM outperforms current state-of-the-art approaches that utilize more complex architectures involving Large Vision-Language-Models, demonstrating the effective generalization ability in an open-set setting and strong robustness to unimodal bias.

