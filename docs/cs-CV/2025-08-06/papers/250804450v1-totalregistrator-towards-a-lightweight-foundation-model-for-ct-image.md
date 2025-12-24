---
layout: default
title: "TotalRegistrator: Towards a Lightweight Foundation Model for CT Image Registration"
---

# TotalRegistrator: Towards a Lightweight Foundation Model for CT Image Registration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04450" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04450v1</a>
  <a href="https://arxiv.org/pdf/2508.04450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04450v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04450v1', 'TotalRegistrator: Towards a Lightweight Foundation Model for CT Image Registration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan Loc Pham, Gwendolyn Vuurberg, Marjan Doppen, Joey Roosen, Tip Stille, Thi Quynh Ha, Thuy Duong Quach, Quoc Vu Dang, Manh Ha Luu, Ewoud J. Smit, Hong Son Mai, Mattias Heinrich, Bram van Ginneken, Mathias Prokop, Alessa Hering

**分类**: eess.IV, cs.CV

**发布日期**: 2025-08-06

**🔗 代码/项目**: [GITHUB](https://github.com/DIAGNijmegen/oncology_image_registration.git)

---

## 💡 一句话要点

**提出TotalRegistrator以解决CT图像多器官配准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像配准` `CT图像` `多器官配准` `UNet架构` `深度学习` `医学影像` `场分解策略`

## 📋 核心要点

1. 现有的图像配准方法多为单一器官设计，缺乏对多器官的通用性，限制了其临床应用。
2. TotalRegistrator通过标准UNet架构和场分解策略，实现了对多个解剖区域的同时配准，具有较低的计算资源需求。
3. 实验结果显示，该方法在多器官腹部配准中优于传统方法，并在外部数据集上表现出竞争力，展示了良好的通用性。

## 📝 摘要（中文）

图像配准是临床实践中分析纵向和多相CT图像的基本技术。然而，大多数现有方法仅针对单一器官应用，限制了其在其他解剖区域的通用性。本研究提出了TotalRegistrator，一个能够同时对多个解剖区域进行配准的图像配准框架，采用标准的UNet架构和新颖的场分解策略。该模型轻量级，训练仅需11GB的GPU内存。我们构建了一个大规模的纵向数据集，包含695个来自不同时间点的全身CT扫描对，并将TotalRegistrator与经典的迭代算法和近期的基础模型进行了基准测试。实验结果表明，该方法在多器官腹部配准中普遍优于基线方法，尽管在肺部对齐性能上略有下降。对外部数据集的评估显示，尽管未针对这些任务进行微调，但仍展现出强大的通用性。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有图像配准方法在多器官配准中的局限性，尤其是针对单一器官的设计导致的通用性不足。

**核心思路**：TotalRegistrator的核心思路是利用UNet架构和场分解策略，能够同时对多个解剖区域进行配准，从而提高配准的效率和准确性。

**技术框架**：该框架包括数据预处理、模型训练和评估三个主要阶段。数据预处理阶段构建了大规模的纵向CT数据集，模型训练阶段采用UNet进行特征提取和配准，评估阶段则通过与基线方法的对比来验证模型性能。

**关键创新**：TotalRegistrator的关键创新在于其轻量级设计和场分解策略，使得模型在保持高效性的同时，能够处理复杂的多器官配准任务。与传统方法相比，该模型在计算资源上具有明显优势。

**关键设计**：模型训练过程中，使用了特定的损失函数以优化配准精度，并在网络结构上进行了调整，以适应多器官的特征提取需求。

## 📊 实验亮点

在实验中，TotalRegistrator在多器官腹部配准中普遍优于经典的迭代算法，且在外部数据集上表现出与领先的单器官模型相当的结果，尽管未进行针对性微调。这表明该模型具有良好的通用性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、肿瘤监测和手术规划等。通过提高多器官CT图像的配准精度，TotalRegistrator能够为临床医生提供更可靠的影像支持，进而改善患者的诊疗效果。未来，该模型的通用性和轻量级特性可能推动其在其他医学影像处理任务中的应用。

## 📄 摘要（原文）

> Image registration is a fundamental technique in the analysis of longitudinal and multi-phase CT images within clinical practice. However, most existing methods are tailored for single-organ applications, limiting their generalizability to other anatomical regions. This work presents TotalRegistrator, an image registration framework capable of aligning multiple anatomical regions simultaneously using a standard UNet architecture and a novel field decomposition strategy. The model is lightweight, requiring only 11GB of GPU memory for training. To train and evaluate our method, we constructed a large-scale longitudinal dataset comprising 695 whole-body (thorax-abdomen-pelvic) paired CT scans from individual patients acquired at different time points. We benchmarked TotalRegistrator against a generic classical iterative algorithm and a recent foundation model for image registration. To further assess robustness and generalizability, we evaluated our model on three external datasets: the public thoracic and abdominal datasets from the Learn2Reg challenge, and a private multiphase abdominal dataset from a collaborating hospital. Experimental results on the in-house dataset show that the proposed approach generally surpasses baseline methods in multi-organ abdominal registration, with a slight drop in lung alignment performance. On out-of-distribution datasets, it achieved competitive results compared to leading single-organ models, despite not being fine-tuned for those tasks, demonstrating strong generalizability. The source code will be publicly available at: https://github.com/DIAGNijmegen/oncology_image_registration.git.

