---
layout: default
title: "CrossJEPA: Cross-Modal Joint-Embedding Predictive Architecture for Efficient 3D Representation Learning from 2D Images"
---

# CrossJEPA: Cross-Modal Joint-Embedding Predictive Architecture for Efficient 3D Representation Learning from 2D Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18424" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18424v1</a>
  <a href="https://arxiv.org/pdf/2511.18424.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18424v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18424v1', 'CrossJEPA: Cross-Modal Joint-Embedding Predictive Architecture for Efficient 3D Representation Learning from 2D Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Avishka Perera, Kumal Hewagamage, Saeedha Nazar, Kavishka Abeywardana, Hasitha Gallella, Ranga Rodrigo, Mohamed Afham

**分类**: cs.CV

**发布日期**: 2025-11-23

**备注**: 24 pages, 10 figures

---

## 💡 一句话要点

**提出CrossJEPA以解决3D表示学习中的2D图像数据稀缺问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `跨模态学习` `3D表示学习` `知识蒸馏` `联合嵌入` `图像基础模型` `高效训练` `模型压缩`

## 📋 核心要点

1. 现有的图像到点云跨模态学习方法在模型规模和训练速度上存在显著不足，导致计算资源消耗高。
2. CrossJEPA通过引入图像基础模型的知识，设计了一种新的联合嵌入预测架构，优化了跨模态学习过程。
3. 在ModelNet40和ScanObjectNN基准测试中，CrossJEPA分别达到了94.2%和88.3%的准确率，展现出优异的性能和效率。

## 📝 摘要（中文）

图像到点云的跨模态学习已成为解决3D表示学习中大规模3D数据集稀缺问题的重要方法。然而，现有利用2D数据的方法往往导致模型庞大且训练缓慢，计算成本高，难以在资源受限的环境中部署。为此，本文提出CrossJEPA，一种简单的跨模态联合嵌入预测架构，利用图像基础模型的知识，训练预测器从对应的3D点云中推断特定渲染2D视图的嵌入。CrossJEPA在合成数据集ModelNet40和真实数据集ScanObjectNN上实现了新的线性探测状态，分别达到94.2%和88.3%的准确率，且仅使用14.1M的预训练参数，展现出高效的内存使用和快速训练的优势。

## 🔬 方法详解

**问题定义**：本文旨在解决3D表示学习中由于缺乏大规模3D数据集而导致的模型训练效率低下和计算资源浪费的问题。现有方法通常需要庞大的模型和长时间的训练，难以在资源受限的环境中应用。

**核心思路**：CrossJEPA的核心思路是利用图像基础模型的知识，通过训练一个预测器来推断特定渲染2D视图的嵌入，从而实现跨模态的联合嵌入学习。这种方法超越了传统的掩蔽策略，提供了一种新的预训练策略。

**技术框架**：CrossJEPA的整体架构包括一个图像基础模型和一个预测器模块。预测器根据跨域投影信息进行条件化，从而提取目标域特有的语义信息。设计中还引入了冻结教师模型和一次性目标嵌入缓存机制，以提高训练效率。

**关键创新**：CrossJEPA的主要创新在于其简化的跨模态联合嵌入预测架构，打破了对掩蔽策略的依赖，利用知识蒸馏技术实现了高效的3D表示学习。与现有方法相比，CrossJEPA在模型规模和训练时间上具有显著优势。

**关键设计**：在设计中，CrossJEPA使用了14.1M的预训练参数，其中点编码器占8.5M，训练时间约为6小时，展现出良好的内存效率和快速训练能力。

## 📊 实验亮点

CrossJEPA在合成数据集ModelNet40上达到了94.2%的线性探测准确率，在真实数据集ScanObjectNN上达到了88.3%。这些结果不仅刷新了现有的性能记录，还表明该方法在参数使用和训练效率上具有显著优势。

## 🎯 应用场景

CrossJEPA在3D表示学习领域具有广泛的应用潜力，尤其是在机器人视觉、自动驾驶、虚拟现实等需要高效处理3D数据的场景中。其高效的训练和内存使用特性使其适合在资源受限的设备上部署，推动了相关技术的实际应用和发展。

## 📄 摘要（原文）

> Image-to-point cross-modal learning has emerged to address the scarcity of large-scale 3D datasets in 3D representation learning. However, current methods that leverage 2D data often result in large, slow-to-train models, making them computationally expensive and difficult to deploy in resource-constrained environments. The architecture design of such models is therefore critical, determining their performance, memory footprint, and compute efficiency. The Joint-embedding Predictive Architecture (JEPA) has gained wide popularity in self-supervised learning for its simplicity and efficiency, but has been under-explored in cross-modal settings, partly due to the misconception that masking is intrinsic to JEPA. In this light, we propose CrossJEPA, a simple Cross-modal Joint Embedding Predictive Architecture that harnesses the knowledge of an image foundation model and trains a predictor to infer embeddings of specific rendered 2D views from corresponding 3D point clouds, thereby introducing a JEPA-style pretraining strategy beyond masking. By conditioning the predictor on cross-domain projection information, CrossJEPA purifies the supervision signal from semantics exclusive to the target domain. We further exploit the frozen teacher design with a one-time target embedding caching mechanism, yielding amortized efficiency. CrossJEPA achieves a new state-of-the-art in linear probing on the synthetic ModelNet40 (94.2%) and the real-world ScanObjectNN (88.3%) benchmarks, using only 14.1M pretraining parameters (8.5M in the point encoder), and about 6 pretraining hours on a standard single GPU. These results position CrossJEPA as a performant, memory-efficient, and fast-to-train framework for 3D representation learning via knowledge distillation. We analyze CrossJEPA intuitively, theoretically, and empirically, and extensively ablate our design choices. Code will be made available.

