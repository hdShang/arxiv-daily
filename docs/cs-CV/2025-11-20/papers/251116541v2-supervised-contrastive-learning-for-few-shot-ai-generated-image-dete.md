---
layout: default
title: Supervised Contrastive Learning for Few-Shot AI-Generated Image Detection and Attribution
---

# Supervised Contrastive Learning for Few-Shot AI-Generated Image Detection and Attribution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16541" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16541v2</a>
  <a href="https://arxiv.org/pdf/2511.16541.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16541v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16541v2', 'Supervised Contrastive Learning for Few-Shot AI-Generated Image Detection and Attribution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaime Álvarez Urueña, David Camacho, Javier Huertas Tato

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-20 (更新: 2025-11-21)

**备注**: 17 pages, 6 figures, 6 tables

---

## 💡 一句话要点

**提出基于监督对比学习的框架，用于少样本AI生成图像检测与溯源。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `监督对比学习` `少样本学习` `AI生成图像检测` `图像溯源` `深度学习` `k近邻分类器` `生成对抗网络`

## 📋 核心要点

1. 现有AI生成图像检测方法依赖定期重新训练，难以跟上新型生成模型快速迭代的步伐，计算成本高昂。
2. 提出一种两阶段框架，利用监督对比学习提取图像嵌入，并使用少样本k-NN分类器进行检测和溯源。
3. 实验结果表明，该框架在少样本情况下显著提升了AI生成图像的检测精度和溯源性能，优于现有方法。

## 📝 摘要（中文）

生成式人工智能的快速发展使得合成图像与真实图像难以区分，给数字媒体的完整性带来了严峻挑战。新型生成模型加速发布周期加剧了这一问题，使得依赖定期重新训练的传统检测方法在计算上不可行，在操作上也不切实际。本文提出了一种新颖的两阶段检测框架，旨在解决合成图像检测中固有的泛化挑战。第一阶段采用通过监督对比学习训练的视觉深度学习模型，从输入图像中提取判别性嵌入。关键在于，该模型在可用生成器的策略性划分的子集上进行训练，并保留特定的架构不参与训练，以严格评估跨生成器的泛化能力。第二阶段利用在学习到的嵌入空间上运行的k近邻（k-NN）分类器，该分类器采用少样本学习范式进行训练，其中包含来自先前未见过的测试生成器的有限样本。在少样本学习机制中，每个类别仅需150张图像（很容易从当前生成模型中获得），所提出的框架即可实现91.3%的平均检测准确率，比现有方法提高了5.2个百分点。对于源溯源任务，在开放集分类上下文中，所提出的方法在AUC和OSCR方面分别获得了14.70%和4.27%的提升，标志着在稳健、可扩展的取证溯源系统方面取得了重大进展，该系统能够适应不断发展的生成式人工智能环境，而无需进行详尽的重新训练协议。

## 🔬 方法详解

**问题定义**：论文旨在解决AI生成图像检测和溯源问题，特别是针对新型生成模型不断涌现，传统检测方法泛化能力不足，需要大量重新训练的问题。现有方法难以适应生成模型的快速变化，计算成本高，效率低。

**核心思路**：论文的核心思路是利用监督对比学习提取具有判别性的图像嵌入，使得来自同一生成器的图像在嵌入空间中更接近，而来自不同生成器的图像更远离。然后，利用少样本学习方法，仅需少量新生成器的样本即可训练分类器，实现快速适应。

**技术框架**：该框架包含两个主要阶段：1) 嵌入提取阶段：使用视觉深度学习模型（如ResNet）在包含多个生成器图像的数据集上进行监督对比学习训练，学习图像的嵌入表示。2) 分类阶段：使用k-NN分类器，在学习到的嵌入空间中，利用少量来自新生成器的样本进行训练，实现对AI生成图像的检测和溯源。

**关键创新**：最重要的技术创新点在于使用监督对比学习来增强模型对不同生成器的泛化能力。通过在训练时将来自同一生成器的图像视为正样本，来自不同生成器的图像视为负样本，模型能够学习到更具判别性的嵌入表示，从而提高对未知生成器的检测准确率。

**关键设计**：在监督对比学习中，使用了对比损失函数，例如InfoNCE loss，来优化嵌入表示。k-NN分类器的k值是一个重要的超参数，需要根据具体数据集进行调整。论文中使用了策略性划分的生成器子集进行训练，并保留部分生成器用于测试，以评估模型的泛化能力。少样本学习中，每个类别使用的样本数量（例如150张）是一个关键参数，影响模型的性能。

## 📊 实验亮点

该框架在少样本学习机制下，每个类别仅需150张图像，平均检测准确率达到91.3%，比现有方法提高了5.2个百分点。在开放集分类的源溯源任务中，AUC指标提升了14.70%，OSCR指标提升了4.27%。实验结果表明，该方法在AI生成图像检测和溯源方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于数字媒体内容安全领域，例如检测和溯源虚假新闻、恶意Deepfake图像等。有助于维护网络信息安全，打击网络犯罪，保护知识产权，提升公众对AI生成内容的辨别能力。未来可扩展到视频、音频等其他模态的AI生成内容检测。

## 📄 摘要（原文）

> The rapid advancement of generative artificial intelligence has enabled the creation of synthetic images that are increasingly indistinguishable from authentic content, posing significant challenges for digital media integrity. This problem is compounded by the accelerated release cycle of novel generative models, which renders traditional detection approaches (reliant on periodic retraining) computationally infeasible and operationally impractical.
>   This work proposes a novel two-stage detection framework designed to address the generalization challenge inherent in synthetic image detection. The first stage employs a vision deep learning model trained via supervised contrastive learning to extract discriminative embeddings from input imagery. Critically, this model was trained on a strategically partitioned subset of available generators, with specific architectures withheld from training to rigorously ablate cross-generator generalization capabilities. The second stage utilizes a k-nearest neighbors (k-NN) classifier operating on the learned embedding space, trained in a few-shot learning paradigm incorporating limited samples from previously unseen test generators.
>   With merely 150 images per class in the few-shot learning regime, which are easily obtainable from current generation models, the proposed framework achieves an average detection accuracy of 91.3%, representing a 5.2 percentage point improvement over existing approaches . For the source attribution task, the proposed approach obtains improvements of of 14.70% and 4.27% in AUC and OSCR respectively on an open set classification context, marking a significant advancement toward robust, scalable forensic attribution systems capable of adapting to the evolving generative AI landscape without requiring exhaustive retraining protocols.

