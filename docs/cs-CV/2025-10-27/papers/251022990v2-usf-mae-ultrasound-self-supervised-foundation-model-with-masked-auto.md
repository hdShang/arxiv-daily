---
layout: default
title: USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding
---

# USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22990" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22990v2</a>
  <a href="https://arxiv.org/pdf/2510.22990.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22990v2" onclick="toggleFavorite(this, '2510.22990v2', 'USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youssef Megahed, Robin Ducharme, Aylin Erman, Mark Walker, Steven Hawken, Adrian D. C. Chan

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-10-27 (更新: 2025-11-07)

**备注**: 18 pages, 8 figures, 2 tables

---

## 💡 一句话要点

**USF-MAE：基于掩码自编码器的超声自监督预训练模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超声图像` `自监督学习` `掩码自编码器` `Vision Transformer` `预训练模型`

## 📋 核心要点

1. 现有深度学习方法受限于缺乏大规模标注超声数据集，且通用图像预训练模型在超声图像上的迁移能力有限。
2. USF-MAE通过掩码自编码器在大量无标注超声数据上进行自监督预训练，学习特定于超声模态的特征表示。
3. 实验表明，USF-MAE在多个超声图像分类任务中显著优于传统CNN和ViT模型，并展现出良好的跨解剖区域泛化能力。

## 📝 摘要（中文）

本文提出了超声自监督基础模型USF-MAE，这是一个大规模的自监督掩码自编码框架，专门用于超声数据。该模型在包含来自46个开源数据集的37万张2D和3D超声图像（OpenUS-46）上进行了预训练，涵盖了20多个解剖区域。OpenUS-46数据集已公开，以促进进一步的研究和可重复性。USF-MAE采用Vision Transformer编码器-解码器架构，通过重建被掩盖的图像块，直接从无标签数据中学习丰富的、特定于模态的表示。预训练的编码器在三个公共下游分类基准（BUS-BRA、MMOTU-2D和GIST514-DB）上进行了微调。在所有任务中，USF-MAE始终优于传统的CNN和ViT基线，分别实现了81.6%、79.6%和82.4%的F1分数。尽管在预训练期间未使用标签，但USF-MAE在乳腺癌分类方面接近了有监督基础模型UltraSam的性能，并在其他任务中超过了它，展示了强大的跨解剖泛化能力。

## 🔬 方法详解

**问题定义**：超声图像诊断面临噪声大、操作者依赖性强、视野有限等挑战，导致观察者间差异大。现有深度学习方法依赖大量标注数据，而超声图像标注成本高昂。通用图像预训练模型在超声图像上的迁移效果不佳，限制了其应用。

**核心思路**：利用掩码自编码器（MAE）进行自监督学习。通过随机掩盖部分超声图像块，并训练模型重建这些被掩盖的区域，迫使模型学习超声图像的内在结构和特征表示。这种方法无需人工标注，可以有效利用大量未标注的超声数据。

**技术框架**：USF-MAE采用Vision Transformer（ViT）作为基础架构，包含一个编码器和一个解码器。编码器处理未被掩盖的图像块，提取特征表示。解码器接收编码器的输出以及被掩盖的图像块的位置信息，重建原始图像。整个流程包括：1）图像块划分与掩码；2）编码器特征提取；3）解码器图像重建；4）损失计算与模型优化。

**关键创新**：USF-MAE是首个专门针对超声数据的、大规模自监督MAE框架。它构建了一个包含46个开源超声数据集的OpenUS-46数据集，为超声领域的自监督学习提供了数据基础。与传统的有监督学习或通用图像预训练模型相比，USF-MAE能够更好地学习超声图像的特定模态特征。

**关键设计**：USF-MAE使用ViT-Base作为编码器和解码器的主干网络。掩码比例设置为75%，即随机掩盖75%的图像块。重建目标为像素值。损失函数采用均方误差（MSE）损失，衡量重建图像与原始图像之间的差异。预训练在OpenUS-46数据集上进行，微调在下游分类任务中使用交叉熵损失。

## 📊 实验亮点

USF-MAE在三个下游分类任务（BUS-BRA、MMOTU-2D和GIST514-DB）上均取得了优异的性能。在BUS-BRA数据集上，USF-MAE的F1分数达到81.6%，接近有监督模型UltraSam的性能。在MMOTU-2D和GIST514-DB数据集上，USF-MAE的F1分数分别为79.6%和82.4%，超过了UltraSam。这些结果表明，USF-MAE具有强大的特征学习能力和跨解剖区域泛化能力。

## 🎯 应用场景

USF-MAE可应用于多种超声图像分析任务，如病灶检测、器官分割、疾病诊断等。通过自监督预训练，可以有效降低对标注数据的依赖，加速超声AI模型的开发和部署。该研究有望提高超声诊断的准确性和效率，并推动超声技术在医疗领域的更广泛应用。

## 📄 摘要（原文）

> Ultrasound imaging is one of the most widely used diagnostic modalities, offering real-time, radiation-free assessment across diverse clinical domains. However, interpretation of ultrasound images remains challenging due to high noise levels, operator dependence, and limited field of view, resulting in substantial inter-observer variability. Current Deep Learning approaches are hindered by the scarcity of large labeled datasets and the domain gap between general and sonographic images, which limits the transferability of models pretrained on non-medical data. To address these challenges, we introduce the Ultrasound Self-Supervised Foundation Model with Masked Autoencoding (USF-MAE), the first large-scale self-supervised MAE framework pretrained exclusively on ultrasound data. The model was pre-trained on 370,000 2D and 3D ultrasound images curated from 46 open-source datasets, collectively termed OpenUS-46, spanning over twenty anatomical regions. This curated dataset has been made publicly available to facilitate further research and reproducibility. Using a Vision Transformer encoder-decoder architecture, USF-MAE reconstructs masked image patches, enabling it to learn rich, modality-specific representations directly from unlabeled data. The pretrained encoder was fine-tuned on three public downstream classification benchmarks: BUS-BRA (breast cancer), MMOTU-2D (ovarian tumors), and GIST514-DB (gastrointestinal stromal tumors). Across all tasks, USF-MAE consistently outperformed conventional CNN and ViT baselines, achieving F1-scores of 81.6%, 79.6%, and 82.4%, respectively. Despite not using labels during pretraining, USF-MAE approached the performance of the supervised foundation model UltraSam on breast cancer classification and surpassed it on the other tasks, demonstrating strong cross-anatomical generalization.

