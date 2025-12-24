---
layout: default
title: "YOLOv11-RGBT: Towards a Comprehensive Single-Stage Multispectral Object Detection Framework"
---

# YOLOv11-RGBT: Towards a Comprehensive Single-Stage Multispectral Object Detection Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14696" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14696v2</a>
  <a href="https://arxiv.org/pdf/2506.14696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14696v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14696v2', 'YOLOv11-RGBT: Towards a Comprehensive Single-Stage Multispectral Object Detection Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dahang Wan, Rongsheng Lu, Yang Fang, Xianli Lang, Shuangbao Shu, Jingjing Chen, Siyuan Shen, Ting Xu, Zecong Ye

**分类**: cs.CV

**发布日期**: 2025-06-17 (更新: 2025-06-18)

**备注**: 29 pages, 8 figures . The errors in the first version have been corrected, and no new version will be submitted in the near future. The next version will include more experiments

**🔗 代码/项目**: [GITHUB](https://github.com/wandahangFY/YOLOv11-RGBT)

---

## 💡 一句话要点

**提出YOLOv11-RGBT以解决多光谱目标检测框架不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多光谱目标检测` `YOLOv11` `特征融合` `可控微调` `深度学习`

## 📋 核心要点

1. 现有多光谱目标检测方法在框架统一性、性能平衡和模态权重分配上存在明显不足。
2. 本文提出YOLOv11-RGBT框架，设计六种多光谱融合模式，并引入P3中融合策略和MCF策略以优化特征融合。
3. 实验结果显示，在FLIR数据集上，YOLOv11模型的mAP提升了3.41%-5.65%，验证了框架和策略的有效性。

## 📝 摘要（中文）

多光谱目标检测通过整合多波段信息，能够提升检测精度和环境适应性，具有广泛的应用潜力。现有方法在跨模态交互、低光照条件和模型轻量化方面取得了一定进展，但仍面临缺乏统一单阶段框架、性能与融合策略平衡困难以及模态权重分配不合理等挑战。为此，基于YOLOv11框架，本文提出了YOLOv11-RGBT，一个新的综合多模态目标检测框架。我们设计了六种多光谱融合模式，并成功应用于YOLOv3至YOLOv12及RT-DETR模型。通过重新评估两种模态的重要性，提出了P3中融合策略和多光谱可控微调（MCF）策略，优化特征融合，减少冗余与不匹配，提升整体模型性能。实验表明，该框架在LLVIP和FLIR等三个主要开源多光谱目标检测数据集上表现优异，特别是多光谱可控微调策略显著增强了模型的适应性和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多光谱目标检测方法缺乏统一单阶段框架、性能与融合策略难以平衡以及模态权重分配不合理等问题。

**核心思路**：提出YOLOv11-RGBT框架，通过设计多种融合模式和引入新的融合策略，优化多光谱特征的融合过程，以提升模型的整体性能和适应性。

**技术框架**：整体架构基于YOLOv11，包含六种多光谱融合模式，P3中融合策略和多光谱可控微调（MCF）策略，旨在优化特征融合和减少冗余。

**关键创新**：最重要的创新在于提出了P3中融合策略和MCF策略，这些策略有效提升了多光谱模型的适应性和鲁棒性，与现有方法相比，显著优化了特征融合过程。

**关键设计**：在模型设计中，采用了多种融合模式，重新评估模态重要性，并通过可控微调策略调整模型参数，以实现更好的性能提升。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

在FLIR数据集上，YOLOv11-RGBT框架显著提升了YOLOv11模型的mAP，提升幅度在3.41%-5.65%之间，最高达到47.61%。这些实验结果验证了提出的框架和策略在多光谱目标检测中的有效性。

## 🎯 应用场景

该研究在多光谱目标检测领域具有广泛的应用潜力，尤其在安防监控、无人驾驶、环境监测等场景中，能够有效提升目标检测的准确性和适应性。未来，该框架的进一步优化和推广将推动多模态融合技术的发展，促进相关应用的智能化进程。

## 📄 摘要（原文）

> Multispectral object detection, which integrates information from multiple bands, can enhance detection accuracy and environmental adaptability, holding great application potential across various fields. Although existing methods have made progress in cross-modal interaction, low-light conditions, and model lightweight, there are still challenges like the lack of a unified single-stage framework, difficulty in balancing performance and fusion strategy, and unreasonable modality weight allocation. To address these, based on the YOLOv11 framework, we present YOLOv11-RGBT, a new comprehensive multimodal object detection framework. We designed six multispectral fusion modes and successfully applied them to models from YOLOv3 to YOLOv12 and RT-DETR. After reevaluating the importance of the two modalities, we proposed a P3 mid-fusion strategy and multispectral controllable fine-tuning (MCF) strategy for multispectral models. These improvements optimize feature fusion, reduce redundancy and mismatches, and boost overall model performance. Experiments show our framework excels on three major open-source multispectral object detection datasets, like LLVIP and FLIR. Particularly, the multispectral controllable fine-tuning strategy significantly enhanced model adaptability and robustness. On the FLIR dataset, it consistently improved YOLOv11 models' mAP by 3.41%-5.65%, reaching a maximum of 47.61%, verifying the framework and strategies' effectiveness. The code is available at: https://github.com/wandahangFY/YOLOv11-RGBT.

