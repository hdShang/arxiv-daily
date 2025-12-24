---
layout: default
title: "DualVision ArthroNav: Investigating Opportunities to Enhance Localization and Reconstruction in Image-based Arthroscopy Navigation via External Cameras"
---

# DualVision ArthroNav: Investigating Opportunities to Enhance Localization and Reconstruction in Image-based Arthroscopy Navigation via External Cameras

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10699" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10699v1</a>
  <a href="https://arxiv.org/pdf/2511.10699.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10699v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10699v1', 'DualVision ArthroNav: Investigating Opportunities to Enhance Localization and Reconstruction in Image-based Arthroscopy Navigation via External Cameras')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongchao Shu, Lalithkumar Seenivasan, Mingxu Liu, Yunseo Hwang, Yu-Chun Ku, Jonathan Knopf, Alejandro Martin-Gomez, Mehran Armand, Mathias Unberath

**分类**: eess.IV, cs.CV, cs.RO

**发布日期**: 2025-11-12

---

## 💡 一句话要点

**DualVision ArthroNav：利用外部相机增强图像引导关节镜导航的定位与重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `关节镜导航` `视觉里程计` `单目SLAM` `多相机融合` `场景重建`

## 📋 核心要点

1. 现有关节镜导航系统依赖光学跟踪，存在工作空间限制和干扰手术流程的问题；纯视觉方案则易受漂移和尺度模糊影响。
2. DualVision ArthroNav通过集成外部相机，提供稳定的视觉里程计和绝对定位，结合关节镜视频进行密集场景重建。
3. 实验表明，该系统有效补偿了校准误差，实现了较低的轨迹误差和目标注册误差，并具有较高的视觉保真度。

## 📝 摘要（中文）

关节镜手术可以从导航系统中获益，从而增强空间感知、深度感知和视野。然而，现有的光学跟踪解决方案对工作空间有严格的限制，并会扰乱手术流程。基于视觉的替代方案虽然侵入性较小，但通常仅依赖于单目关节镜相机，容易出现漂移、尺度模糊以及对快速运动或遮挡的敏感性。我们提出了DualVision ArthroNav，一种多相机关节镜导航系统，它集成了一个刚性安装在关节镜上的外部相机。外部相机提供稳定的视觉里程计和绝对定位，而单目关节镜视频则能够实现密集的场景重建。通过结合这些互补的视图，我们的系统解决了单目SLAM中固有的尺度模糊和长期漂移问题，并确保了鲁棒的重定位。实验表明，我们的系统有效地补偿了校准误差，实现了1.09毫米的平均绝对轨迹误差。重建的场景达到了2.16毫米的平均目标注册误差，具有很高的视觉保真度（SSIM = 0.69，PSNR = 22.19）。这些结果表明，我们的系统为关节镜导航提供了一种实用且经济高效的解决方案，弥合了光学跟踪和纯视觉系统之间的差距，并为临床可部署的、完全基于视觉的关节镜引导铺平了道路。

## 🔬 方法详解

**问题定义**：现有基于单目视觉的关节镜导航系统，由于缺乏全局信息，容易产生尺度漂移和累积误差，导致定位精度下降，无法满足临床手术的需求。光学跟踪方案虽然精度高，但存在工作空间限制，且会干扰手术流程。因此，需要一种既能保证精度，又能避免外部设备干扰的关节镜导航方案。

**核心思路**：DualVision ArthroNav的核心思路是融合关节镜内部视角和外部视角的信息，利用外部相机提供全局的、稳定的定位信息，解决单目视觉的尺度模糊和漂移问题；同时，利用关节镜内部视角进行高精度的局部场景重建。通过互补的视角信息，实现鲁棒且精确的关节镜导航。

**技术框架**：DualVision ArthroNav系统包含两个主要模块：外部相机视觉里程计模块和关节镜场景重建模块。外部相机视觉里程计模块负责估计关节镜的全局位姿，提供稳定的定位信息。关节镜场景重建模块利用单目SLAM技术，重建关节镜视野内的三维场景。最后，通过融合两个模块的信息，实现精确的关节镜导航。

**关键创新**：该论文的关键创新在于提出了DualVision ArthroNav，一种多相机融合的关节镜导航系统。与传统的单目视觉方案相比，该系统能够有效解决尺度模糊和漂移问题，提高定位精度和鲁棒性。与光学跟踪方案相比，该系统无需外部设备，避免了对工作空间的限制和手术流程的干扰。

**关键设计**：外部相机与关节镜刚性连接，保证了两个相机之间的相对位姿不变。系统采用基于优化的视觉里程计算法，估计外部相机的位姿。关节镜场景重建模块采用单目SLAM算法，并结合外部相机的位姿信息进行全局优化。实验中，通过精心设计的校准流程，减小了相机之间的校准误差。

## 📊 实验亮点

实验结果表明，DualVision ArthroNav能够有效补偿校准误差，实现平均1.09毫米的绝对轨迹误差。重建的场景达到了2.16毫米的平均目标注册误差，具有较高的视觉保真度（SSIM = 0.69，PSNR = 22.19）。这些结果表明，该系统在关节镜导航中具有较高的精度和鲁棒性，优于传统的单目视觉方案。

## 🎯 应用场景

DualVision ArthroNav可应用于各种关节镜手术，例如膝关节、肩关节和髋关节手术。该系统能够提高手术的精确性和安全性，减少手术时间和并发症。此外，该技术还可以扩展到其他内窥镜手术，例如腹腔镜手术和胸腔镜手术，具有广阔的应用前景。

## 📄 摘要（原文）

> Arthroscopic procedures can greatly benefit from navigation systems that enhance spatial awareness, depth perception, and field of view. However, existing optical tracking solutions impose strict workspace constraints and disrupt surgical workflow. Vision-based alternatives, though less invasive, often rely solely on the monocular arthroscope camera, making them prone to drift, scale ambiguity, and sensitivity to rapid motion or occlusion. We propose DualVision ArthroNav, a multi-camera arthroscopy navigation system that integrates an external camera rigidly mounted on the arthroscope. The external camera provides stable visual odometry and absolute localization, while the monocular arthroscope video enables dense scene reconstruction. By combining these complementary views, our system resolves the scale ambiguity and long-term drift inherent in monocular SLAM and ensures robust relocalization. Experiments demonstrate that our system effectively compensates for calibration errors, achieving an average absolute trajectory error of 1.09 mm. The reconstructed scenes reach an average target registration error of 2.16 mm, with high visual fidelity (SSIM = 0.69, PSNR = 22.19). These results indicate that our system provides a practical and cost-efficient solution for arthroscopic navigation, bridging the gap between optical tracking and purely vision-based systems, and paving the way toward clinically deployable, fully vision-based arthroscopic guidance.

