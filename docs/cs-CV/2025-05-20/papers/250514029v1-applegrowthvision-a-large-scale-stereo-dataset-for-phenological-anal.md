---
layout: default
title: "AppleGrowthVision: A large-scale stereo dataset for phenological analysis, fruit detection, and 3D reconstruction in apple orchards"
---

# AppleGrowthVision: A large-scale stereo dataset for phenological analysis, fruit detection, and 3D reconstruction in apple orchards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14029" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14029v1</a>
  <a href="https://arxiv.org/pdf/2505.14029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14029v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14029v1', 'AppleGrowthVision: A large-scale stereo dataset for phenological analysis, fruit detection, and 3D reconstruction in apple orchards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Laura-Sophia von Hirschhausen, Jannes S. Magnusson, Mykyta Kovalenko, Fredrik Boye, Tanay Rawat, Peter Eisert, Anna Hilsmann, Sebastian Pretzsch, Sebastian Bosse

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出AppleGrowthVision以解决苹果园监测数据集不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `苹果园监测` `深度学习` `数据集` `3D重建` `物候分析` `果实检测` `精准农业` `计算机视觉`

## 📋 核心要点

1. 现有苹果园监测方法受限于数据集的多样性和真实感，难以进行有效的生长阶段分析和果实定位。
2. 本文提出AppleGrowthVision数据集，包含高分辨率立体图像和密集注释，支持精确的物候分析和3D重建。
3. 实验结果表明，使用AppleGrowthVision数据集，YOLOv8的F1-score提升了7.69%，Faster R-CNN的F1-score提升了31.06%。

## 📝 摘要（中文）

深度学习已改变精准农业的计算机视觉，但苹果园监测仍受限于数据集的约束。现有数据集缺乏多样性和真实感，且难以注释密集异质场景。为填补这些空白，本文提出了AppleGrowthVision，一个大规模数据集，包含两个子集：第一部分为来自德国勃兰登堡的9317张高分辨率立体图像，涵盖六个经过农业验证的生长阶段；第二部分为1125张密集注释图像，包含31084个苹果标签。AppleGrowthVision为精准的物候分析和3D重建提供了立体图像数据，显著提升了YOLOv8和Faster R-CNN的性能。未来工作将集中在改进注释和增强3D重建等方面。

## 🔬 方法详解

**问题定义**：本文旨在解决苹果园监测中缺乏多样化和真实感数据集的问题，现有数据集无法有效支持不同生长阶段的分析和果实定位。

**核心思路**：提出AppleGrowthVision数据集，通过收集高分辨率立体图像和密集注释，填补现有数据集的不足，支持更精准的农业分析和3D重建。

**技术框架**：数据集分为两个子集：第一部分为9317张高分辨率立体图像，覆盖六个生长阶段；第二部分为1125张密集注释图像，包含31084个苹果标签。数据集的设计旨在提供丰富的样本以支持深度学习模型的训练。

**关键创新**：AppleGrowthVision的主要创新在于其大规模的立体图像数据和详细的生长阶段注释，显著提高了模型在果实检测和生长建模中的表现。

**关键设计**：在实验中，使用了YOLOv8和Faster R-CNN等深度学习模型，结合VGG16、ResNet152等网络结构进行训练，优化了损失函数和参数设置，以提升模型的准确性和鲁棒性。

## 📊 实验亮点

实验结果显示，使用AppleGrowthVision数据集，YOLOv8的F1-score提升了7.69%，而结合MinneApple和MAD后，Faster R-CNN的F1-score提升了31.06%。此外，使用VGG16等模型对六个BBCH生长阶段的预测准确率超过95%。

## 🎯 应用场景

AppleGrowthVision数据集的潜在应用领域包括精准农业中的果实检测、产量估算和生长建模。通过提供高质量的数据，研究人员和农业从业者可以开发更为精确的监测工具，推动农业科学与计算机视觉的结合，提升农业生产效率和可持续性。

## 📄 摘要（原文）

> Deep learning has transformed computer vision for precision agriculture, yet apple orchard monitoring remains limited by dataset constraints. The lack of diverse, realistic datasets and the difficulty of annotating dense, heterogeneous scenes. Existing datasets overlook different growth stages and stereo imagery, both essential for realistic 3D modeling of orchards and tasks like fruit localization, yield estimation, and structural analysis. To address these gaps, we present AppleGrowthVision, a large-scale dataset comprising two subsets. The first includes 9,317 high resolution stereo images collected from a farm in Brandenburg (Germany), covering six agriculturally validated growth stages over a full growth cycle. The second subset consists of 1,125 densely annotated images from the same farm in Brandenburg and one in Pillnitz (Germany), containing a total of 31,084 apple labels. AppleGrowthVision provides stereo-image data with agriculturally validated growth stages, enabling precise phenological analysis and 3D reconstructions. Extending MinneApple with our data improves YOLOv8 performance by 7.69 % in terms of F1-score, while adding it to MinneApple and MAD boosts Faster R-CNN F1-score by 31.06 %. Additionally, six BBCH stages were predicted with over 95 % accuracy using VGG16, ResNet152, DenseNet201, and MobileNetv2. AppleGrowthVision bridges the gap between agricultural science and computer vision, by enabling the development of robust models for fruit detection, growth modeling, and 3D analysis in precision agriculture. Future work includes improving annotation, enhancing 3D reconstruction, and extending multimodal analysis across all growth stages.

