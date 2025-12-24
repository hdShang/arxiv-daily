---
layout: default
title: "SingRef6D: Monocular Novel Object Pose Estimation with a Single RGB Reference"
---

# SingRef6D: Monocular Novel Object Pose Estimation with a Single RGB Reference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21927" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21927v1</a>
  <a href="https://arxiv.org/pdf/2509.21927.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21927v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21927v1', 'SingRef6D: Monocular Novel Object Pose Estimation with a Single RGB Reference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Wang, Haiyue Zhu, Haoren Guo, Abdullah Al Mamun, Cheng Xiang, Tong Heng Lee

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: Accepted as a poster in NeurIPS 2025

---

## 💡 一句话要点

**SingRef6D：基于单张RGB参考图像的新物体单目6D位姿估计**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `6D位姿估计` `单目视觉` `深度预测` `特征匹配` `机器人抓取`

## 📋 核心要点

1. 现有6D位姿估计方法依赖深度信息，在透明或高反射材质上失效；RGB方法在弱光和无纹理场景中匹配性能较差。
2. SingRef6D仅使用单张RGB图像作为参考，通过深度预测和深度感知匹配，提升在复杂场景下的位姿估计鲁棒性。
3. 实验表明，SingRef6D在深度预测和位姿估计方面均优于现有方法，并在多个数据集上取得了显著的性能提升。

## 📝 摘要（中文）

本文提出SingRef6D，一个轻量级的单目6D位姿估计流程，仅需单张RGB参考图像，无需深度传感器、多视角图像或训练视角合成模型与神经场。这使得SingRef6D在资源受限、深度或密集模板不可用的情况下依然稳健。该框架包含两项关键创新：一是基于token-scaler的微调机制，结合新的优化损失，增强Depth-Anything v2预测精确深度的能力，尤其针对复杂表面。在REAL275数据集上，深度预测精度($δ_{1.05}$)相比微调后的Depth-Anything v2提升14.41%。二是引入深度感知的匹配过程，有效整合LoFTR中的空间关系，从而处理具有挑战性的材质和光照条件下的匹配。在REAL275、ClearPose和Toyota-Light数据集上的位姿估计评估表明，该方法超越了现有技术，平均召回率提升6.1%。

## 🔬 方法详解

**问题定义**：现有6D位姿估计方法面临实际应用限制。依赖深度信息的方法在处理透明、高反射等材质时性能下降。纯RGB方法在弱光照、无纹理场景下，由于缺乏几何信息，匹配精度不高。这些问题限制了6D位姿估计在资源受限环境下的应用。

**核心思路**：SingRef6D的核心思路是利用单张RGB图像，通过深度预测模块获得场景的深度信息，然后利用深度信息辅助特征匹配，从而提升位姿估计的鲁棒性。这种方法避免了对深度传感器的依赖，也无需复杂的视角合成或神经场建模。

**技术框架**：SingRef6D主要包含两个阶段：1) 深度预测阶段：使用改进的Depth-Anything v2模型预测场景深度图。该模型通过token-scaler微调机制和新的优化损失函数进行训练，以提高深度预测精度。2) 位姿估计阶段：利用预测的深度图，结合LoFTR进行深度感知的特征匹配。匹配结果用于估计物体的6D位姿。

**关键创新**：该论文的关键创新在于两个方面：一是提出了基于token-scaler的深度预测微调机制，有效提升了Depth-Anything v2在复杂材质上的深度预测精度。二是引入了深度感知的匹配过程，将深度信息融入到LoFTR的特征匹配中，从而提高了匹配的鲁棒性。与现有方法相比，SingRef6D无需深度传感器或多视角图像，更加轻量级和实用。

**关键设计**：在深度预测阶段，采用了token-scaler微调机制，具体实现细节未知。优化损失函数的设计也未知。在深度感知的匹配过程中，如何将深度信息有效地融入到LoFTR的特征匹配中，具体实现细节未知。这些细节对最终的性能至关重要。

## 📊 实验亮点

SingRef6D在REAL275数据集上，深度预测精度($δ_{1.05}$)相比微调后的Depth-Anything v2提升14.41%。在REAL275、ClearPose和Toyota-Light数据集上的位姿估计评估表明，该方法超越了现有技术，平均召回率提升6.1%。这些结果表明SingRef6D在深度预测和位姿估计方面均具有显著优势。

## 🎯 应用场景

SingRef6D适用于机器人抓取、增强现实、自动驾驶等领域。在这些场景中，获取精确的物体位姿至关重要。由于SingRef6D仅需单张RGB图像，因此可以在资源受限的环境中部署，例如移动机器人或嵌入式系统。该研究的未来影响在于推动6D位姿估计在更广泛的实际场景中的应用。

## 📄 摘要（原文）

> Recent 6D pose estimation methods demonstrate notable performance but still face some practical limitations. For instance, many of them rely heavily on sensor depth, which may fail with challenging surface conditions, such as transparent or highly reflective materials. In the meantime, RGB-based solutions provide less robust matching performance in low-light and texture-less scenes due to the lack of geometry information. Motivated by these, we propose SingRef6D, a lightweight pipeline requiring only a single RGB image as a reference, eliminating the need for costly depth sensors, multi-view image acquisition, or training view synthesis models and neural fields. This enables SingRef6D to remain robust and capable even under resource-limited settings where depth or dense templates are unavailable. Our framework incorporates two key innovations. First, we propose a token-scaler-based fine-tuning mechanism with a novel optimization loss on top of Depth-Anything v2 to enhance its ability to predict accurate depth, even for challenging surfaces. Our results show a 14.41% improvement (in $δ_{1.05}$) on REAL275 depth prediction compared to Depth-Anything v2 (with fine-tuned head). Second, benefiting from depth availability, we introduce a depth-aware matching process that effectively integrates spatial relationships within LoFTR, enabling our system to handle matching for challenging materials and lighting conditions. Evaluations of pose estimation on the REAL275, ClearPose, and Toyota-Light datasets show that our approach surpasses state-of-the-art methods, achieving a 6.1% improvement in average recall.

