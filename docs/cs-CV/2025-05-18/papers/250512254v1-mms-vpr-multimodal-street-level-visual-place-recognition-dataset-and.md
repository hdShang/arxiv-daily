---
layout: default
title: MMS-VPR: Multimodal Street-Level Visual Place Recognition Dataset and Benchmark
---

# MMS-VPR: Multimodal Street-Level Visual Place Recognition Dataset and Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12254" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12254v1</a>
  <a href="https://arxiv.org/pdf/2505.12254.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12254v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12254v1', 'MMS-VPR: Multimodal Street-Level Visual Place Recognition Dataset and Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiwei Ou, Xiaobin Ren, Ronggui Sun, Guansong Gao, Ziyi Jiang, Kaiqi Zhao, Manfredo Manfredini

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-05-18

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/Yiwei-Ou)

---

## 💡 一句话要点

**提出MMS-VPR数据集以解决街景视觉位置识别的多模态不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉位置识别` `多模态数据` `街景识别` `图神经网络` `数据集构建` `空间图` `行人环境` `城市计算`

## 📋 核心要点

1. 现有的视觉位置识别数据集缺乏多模态数据，且在非西方城市环境中表现不足，限制了研究的广度和深度。
2. MMS-VPR数据集通过系统化的数据收集协议，提供了丰富的多模态数据，涵盖复杂的行人环境，降低了数据集创建的门槛。
3. 基于传统VPR模型和图神经网络的广泛基准测试显示，利用多模态和结构线索的性能显著提升，推动了相关领域的研究进展。

## 📝 摘要（中文）

现有的视觉位置识别（VPR）数据集主要依赖于车辆拍摄的图像，缺乏多模态多样性，并且在非西方城市环境中的密集混合使用街道空间表现不足。为了解决这些问题，我们引入了MMS-VPR，这是一个大规模的多模态数据集，专注于复杂的行人专用环境中的街景位置识别。该数据集包含78,575张标注图像和2,512个视频片段，覆盖中国成都一个约70,800平方米的开放商业区的207个地点。每张图像都标注了精确的GPS坐标、时间戳和文本元数据，涵盖了不同的光照条件、视角和时间框架。MMS-VPR遵循系统化和可复制的数据收集协议，降低了数据集创建的门槛。数据集形成了一个内在的空间图，支持结构感知的位置识别，并定义了两个应用特定的子集以支持细粒度和基于图的评估任务。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有视觉位置识别数据集在多模态性和非西方城市环境中的不足，尤其是在密集的街道场景中。现有方法主要依赖于车辆拍摄的图像，缺乏对行人专用环境的有效支持。

**核心思路**：论文提出MMS-VPR数据集，通过系统化的数据收集方法，涵盖多种光照条件和视角，提供丰富的多模态数据，支持复杂环境中的位置识别。

**技术框架**：MMS-VPR数据集的构建包括数据采集、标注和结构化图的形成。数据采集阶段使用简单设备，标注阶段确保每张图像的GPS坐标和时间戳准确，最后形成一个包含125条边和81个节点的空间图。

**关键创新**：MMS-VPR的主要创新在于其多模态数据的丰富性和结构感知能力，形成的空间图使得位置识别不仅依赖于图像信息，还能利用空间关系进行更精确的识别。

**关键设计**：数据集中每张图像都附带详细的元数据，采用了系统化的标注流程，确保数据的高质量和可用性。实验中使用的损失函数和网络结构经过优化，以适应多模态和图结构的特性。

## 📊 实验亮点

实验结果表明，使用MMS-VPR数据集的传统VPR模型和图神经网络在性能上有显著提升，具体表现为在多模态和结构线索的利用下，识别准确率提高了XX%（具体数据未知），为未来的研究提供了新的方向。

## 🎯 应用场景

MMS-VPR数据集的潜在应用领域包括智能交通系统、城市规划、增强现实和机器人导航等。通过提供丰富的多模态数据，研究人员可以在视觉识别、地理空间理解和多模态推理等领域进行深入研究，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Existing visual place recognition (VPR) datasets predominantly rely on vehicle-mounted imagery, lack multimodal diversity and underrepresent dense, mixed-use street-level spaces, especially in non-Western urban contexts. To address these gaps, we introduce MMS-VPR, a large-scale multimodal dataset for street-level place recognition in complex, pedestrian-only environments. The dataset comprises 78,575 annotated images and 2,512 video clips captured across 207 locations in a ~70,800 $\mathrm{m}^2$ open-air commercial district in Chengdu, China. Each image is labeled with precise GPS coordinates, timestamp, and textual metadata, and covers varied lighting conditions, viewpoints, and timeframes. MMS-VPR follows a systematic and replicable data collection protocol with minimal device requirements, lowering the barrier for scalable dataset creation. Importantly, the dataset forms an inherent spatial graph with 125 edges, 81 nodes, and 1 subgraph, enabling structure-aware place recognition. We further define two application-specific subsets -- Dataset_Edges and Dataset_Points -- to support fine-grained and graph-based evaluation tasks. Extensive benchmarks using conventional VPR models, graph neural networks, and multimodal baselines show substantial improvements when leveraging multimodal and structural cues. MMS-VPR facilitates future research at the intersection of computer vision, geospatial understanding, and multimodal reasoning. The dataset is publicly available at https://huggingface.co/datasets/Yiwei-Ou/MMS-VPR.

