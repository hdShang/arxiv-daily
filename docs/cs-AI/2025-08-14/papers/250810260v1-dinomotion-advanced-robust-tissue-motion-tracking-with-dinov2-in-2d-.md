---
layout: default
title: "DINOMotion: advanced robust tissue motion tracking with DINOv2 in 2D-Cine MRI-guided radiotherapy"
---

# DINOMotion: advanced robust tissue motion tracking with DINOv2 in 2D-Cine MRI-guided radiotherapy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10260" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10260v1</a>
  <a href="https://arxiv.org/pdf/2508.10260.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10260v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10260v1', 'DINOMotion: advanced robust tissue motion tracking with DINOv2 in 2D-Cine MRI-guided radiotherapy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soorena Salari, Catherine Spino, Laurie-Anne Pharand, Fabienne Lathuiliere, Hassan Rivaz, Silvain Beriault, Yiming Xiao

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-08-14

**备注**: Accepted to IEEE Transactions on Biomedical Engineering (TMBE), 14 pages

---

## 💡 一句话要点

**提出DINOMotion以解决2D-Cine MRI引导放疗中的组织运动跟踪问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `组织运动跟踪` `MRI引导放疗` `深度学习` `图像配准` `DINOv2` `低秩适应` `实时处理` `可解释性`

## 📋 核心要点

1. 现有的图像配准方法在处理大幅错位时常常面临挑战，且缺乏可解释性，影响了放疗的安全性与效果。
2. DINOMotion通过自动检测地标实现图像配准，结合LoRA层提高训练效率，并利用DINOv2的特征表示增强鲁棒性。
3. 实验结果显示，DINOMotion在肾脏、肝脏和肺部的Dice分数分别达到92.07%、90.90%和95.23%，处理每个扫描的时间约为30毫秒。

## 📝 摘要（中文）

准确的组织运动跟踪对于确保2D-Cine MRI引导放疗的治疗效果和安全性至关重要。传统方法通常依赖于序列图像的配准，但在大幅错位和缺乏可解释性方面面临挑战。本文提出了DINOMotion，一个基于DINOv2和低秩适应（LoRA）层的深度学习框架，旨在实现稳健、高效且可解释的运动跟踪。DINOMotion自动检测对应的地标以推导最佳图像配准，通过提供序列图像之间的显式视觉对应关系来增强可解释性。LoRA层的集成减少了可训练参数，提高了训练效率，而DINOv2强大的特征表示则增强了对大幅错位的鲁棒性。实验结果表明，DINOMotion在处理大幅错位时表现优异，显示出其在实时运动跟踪中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决2D-Cine MRI引导放疗中组织运动跟踪的准确性问题。现有方法在大幅错位情况下表现不佳，且缺乏可解释性，限制了其临床应用。

**核心思路**：DINOMotion通过引入DINOv2和LoRA层，自动检测图像中的对应地标，从而实现高效且可解释的图像配准。该方法直接在测试时计算图像配准，避免了迭代优化的复杂性。

**技术框架**：DINOMotion的整体架构包括图像输入模块、地标检测模块、图像配准模块和输出结果模块。通过LoRA层的集成，减少了模型的可训练参数，提高了训练效率。

**关键创新**：DINOMotion的主要创新在于结合了DINOv2的强大特征表示和LoRA层的高效性，使得模型在处理大幅错位时表现出色，并提供了可解释的视觉对应关系。

**关键设计**：在设计中，DINOMotion使用了低秩适应（LoRA）层来减少参数量，同时采用了特定的损失函数来优化图像配准的准确性。网络结构上，DINOv2的特征提取能力被充分利用，以增强模型的鲁棒性。

## 📊 实验亮点

DINOMotion在肾脏、肝脏和肺部的Dice分数分别达到92.07%、90.90%和95.23%，Hausdorff距离为5.47 mm、8.31 mm和6.72 mm，处理每个扫描的时间约为30毫秒，显著优于现有的最先进方法，尤其在处理大幅错位时表现突出。

## 🎯 应用场景

DINOMotion的研究成果在放射治疗领域具有重要应用潜力，尤其是在需要实时组织运动跟踪的2D-Cine MRI引导放疗中。其高效性和可解释性使得临床医生能够更好地理解和控制治疗过程，从而提高患者的安全性和治疗效果。未来，该方法还可扩展到其他医学成像和治疗领域。

## 📄 摘要（原文）

> Accurate tissue motion tracking is critical to ensure treatment outcome and safety in 2D-Cine MRI-guided radiotherapy. This is typically achieved by registration of sequential images, but existing methods often face challenges with large misalignments and lack of interpretability. In this paper, we introduce DINOMotion, a novel deep learning framework based on DINOv2 with Low-Rank Adaptation (LoRA) layers for robust, efficient, and interpretable motion tracking. DINOMotion automatically detects corresponding landmarks to derive optimal image registration, enhancing interpretability by providing explicit visual correspondences between sequential images. The integration of LoRA layers reduces trainable parameters, improving training efficiency, while DINOv2's powerful feature representations offer robustness against large misalignments. Unlike iterative optimization-based methods, DINOMotion directly computes image registration at test time. Our experiments on volunteer and patient datasets demonstrate its effectiveness in estimating both linear and nonlinear transformations, achieving Dice scores of 92.07% for the kidney, 90.90% for the liver, and 95.23% for the lung, with corresponding Hausdorff distances of 5.47 mm, 8.31 mm, and 6.72 mm, respectively. DINOMotion processes each scan in approximately 30ms and consistently outperforms state-of-the-art methods, particularly in handling large misalignments. These results highlight its potential as a robust and interpretable solution for real-time motion tracking in 2D-Cine MRI-guided radiotherapy.

