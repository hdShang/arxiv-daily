---
layout: default
title: "SphereDrag: Spherical Geometry-Aware Panoramic Image Editing"
---

# SphereDrag: Spherical Geometry-Aware Panoramic Image Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11863" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11863v2</a>
  <a href="https://arxiv.org/pdf/2506.11863.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11863v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11863v2', 'SphereDrag: Spherical Geometry-Aware Panoramic Image Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiao Feng, Xuewei Li, Junjie Yang, Jingchao Li, Yuxin Peng, Xi Li

**分类**: cs.CV

**发布日期**: 2025-06-13 (更新: 2025-10-16)

**备注**: Accepted by PRCV 2025

---

## 💡 一句话要点

**提出SphereDrag以解决全景图像编辑中的几何问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `全景图像编辑` `球面几何` `自适应重投影` `轨迹调整` `像素密度均匀性`

## 📋 核心要点

1. 全景图像编辑面临边界不连续、轨迹变形和像素密度不均等挑战，现有方法难以有效解决这些问题。
2. SphereDrag通过自适应重投影、大圆轨迹调整和球面搜索区域跟踪等技术，利用球面几何知识实现精确编辑。
3. 实验结果显示，SphereDrag在几何一致性和图像质量上相比现有方法有10.5%的相对提升，表现出显著的优势。

## 📝 摘要（中文）

图像编辑在平面图像上取得了显著进展，但全景图像编辑仍然未被充分探索。全景图像由于其球面几何和投影失真，面临边界不连续、轨迹变形和像素密度不均等三大挑战。为了解决这些问题，本文提出了SphereDrag，这是一种利用球面几何知识进行精确和可控编辑的新型全景编辑框架。具体而言，自适应重投影（AR）通过自适应球面旋转处理不连续性；大圆轨迹调整（GCTA）更准确地跟踪运动轨迹；球面搜索区域跟踪（SSRT）根据球面位置自适应缩放搜索范围，以解决像素密度不均的问题。此外，我们构建了PanoBench，一个包含多个对象和多样风格的复杂编辑任务的全景编辑基准，为标准化评估框架提供支持。实验表明，SphereDrag在几何一致性和图像质量方面相比现有方法有显著提升，达到10.5%的相对改善。

## 🔬 方法详解

**问题定义**：全景图像编辑中，由于球面几何和投影失真，存在边界不连续、轨迹变形和像素密度不均等问题，现有方法无法有效处理这些挑战。

**核心思路**：SphereDrag的核心思路是利用球面几何知识，通过自适应重投影和轨迹调整等技术，提供更为精确和可控的全景图像编辑能力。

**技术框架**：SphereDrag的整体架构包括三个主要模块：自适应重投影（AR）模块处理边界不连续性；大圆轨迹调整（GCTA）模块精确跟踪运动轨迹；球面搜索区域跟踪（SSRT）模块根据球面位置自适应调整搜索范围。

**关键创新**：SphereDrag的关键创新在于结合了自适应重投影和大圆轨迹调整技术，能够有效解决全景图像编辑中的几何一致性问题，与传统方法相比具有本质区别。

**关键设计**：在设计中，AR模块采用自适应球面旋转，GCTA模块通过改进的轨迹跟踪算法实现更高精度，SSRT模块则根据像素密度动态调整搜索范围，确保编辑效果的均匀性。

## 📊 实验亮点

实验结果表明，SphereDrag在几何一致性和图像质量方面相比现有方法有显著提升，具体表现为相对改善达10.5%。该方法在处理复杂编辑任务时表现出更高的准确性和可控性，优于基线方法。

## 🎯 应用场景

SphereDrag的研究成果可广泛应用于虚拟现实、增强现实和全景视频制作等领域，为用户提供更高质量的全景图像编辑体验。随着全景图像技术的普及，该方法的实际价值和影响将愈加显著，推动相关行业的发展。

## 📄 摘要（原文）

> Image editing has made great progress on planar images, but panoramic image editing remains underexplored. Due to their spherical geometry and projection distortions, panoramic images present three key challenges: boundary discontinuity, trajectory deformation, and uneven pixel density. To tackle these issues, we propose SphereDrag, a novel panoramic editing framework utilizing spherical geometry knowledge for accurate and controllable editing. Specifically, adaptive reprojection (AR) uses adaptive spherical rotation to deal with discontinuity; great-circle trajectory adjustment (GCTA) tracks the movement trajectory more accurate; spherical search region tracking (SSRT) adaptively scales the search range based on spherical location to address uneven pixel density. Also, we construct PanoBench, a panoramic editing benchmark, including complex editing tasks involving multiple objects and diverse styles, which provides a standardized evaluation framework. Experiments show that SphereDrag gains a considerable improvement compared with existing methods in geometric consistency and image quality, achieving up to 10.5% relative improvement.

