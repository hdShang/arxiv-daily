---
layout: default
title: Geo6DPose: Fast Zero-Shot 6D Object Pose Estimation via Geometry-Filtered Feature Matching
---

# Geo6DPose: Fast Zero-Shot 6D Object Pose Estimation via Geometry-Filtered Feature Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10674" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10674v1</a>
  <a href="https://arxiv.org/pdf/2512.10674.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10674v1" onclick="toggleFavorite(this, '2512.10674v1', 'Geo6DPose: Fast Zero-Shot 6D Object Pose Estimation via Geometry-Filtered Feature Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javier Villena Toro, Mehdi Tarkian

**分类**: cs.CV

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**Geo6DPose：基于几何滤波特征匹配的快速零样本6D物体姿态估计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `6D姿态估计` `零样本学习` `几何滤波` `机器人视觉` `特征匹配`

## 📋 核心要点

1. 现有零样本6D姿态估计方法依赖大规模模型和云端推理，导致高延迟、高能耗，不适用于算力受限的机器人应用。
2. Geo6DPose利用几何滤波策略，结合基础模型视觉特征，构建轻量级、全本地、免训练的6D姿态估计流程。
3. 实验表明，Geo6DPose在单个GPU上实现亚秒级推理，同时达到与大型零样本基线相当的平均召回率。

## 📝 摘要（中文）

本文提出Geo6DPose，一个轻量级、全本地、免训练的零样本6D姿态估计流程，通过几何可靠性替代模型规模。该方法结合了基础模型视觉特征和几何滤波策略：计算板载模板DINO描述符与场景块之间的相似度图，并通过将场景块中心投影到3D和模板描述符投影到物体模型坐标系来建立互对应关系。最终姿态通过对应关系驱动的RANSAC恢复，并使用加权几何对齐度量进行排序，该度量共同考虑了重投影一致性和空间支持，从而提高对噪声、杂乱和部分可见性的鲁棒性。Geo6DPose在单个商用GPU上实现了亚秒级推理，同时匹配了显著更大的零样本基线的平均召回率（53.7 AR，1.08 FPS）。它不需要训练、微调或网络访问，并且与不断发展的基础骨干网络兼容，从而推进了用于机器人部署的实用、完全本地的6D感知。

## 🔬 方法详解

**问题定义**：零样本6D物体姿态估计旨在无需针对特定物体进行训练的情况下，估计场景中物体的6D姿态（位置和方向）。现有方法通常依赖于大型预训练模型和云端计算，这导致了高延迟、高能耗以及对网络连接的依赖，不适用于资源受限的机器人应用场景。因此，如何在本地设备上实现快速、高效的零样本6D姿态估计是一个关键问题。

**核心思路**：Geo6DPose的核心思路是利用几何信息来弥补模型规模的不足。通过结合基础模型的视觉特征和几何滤波策略，该方法能够有效地建立场景和物体模型之间的对应关系，并从中恢复准确的6D姿态。这种方法避免了对大型模型的依赖，从而实现了轻量级和快速的推理。

**技术框架**：Geo6DPose的整体流程包括以下几个主要阶段：
1. **特征提取**：使用预训练的DINO模型提取场景图像和物体模板的视觉特征。
2. **相似度计算**：计算场景块和模板描述符之间的相似度图。
3. **对应关系建立**：将场景块中心投影到3D空间，并将模板描述符投影到物体模型坐标系，从而建立场景和物体模型之间的互对应关系。
4. **姿态恢复**：使用RANSAC算法，基于建立的对应关系恢复物体的6D姿态。
5. **姿态排序**：使用加权几何对齐度量对恢复的姿态进行排序，该度量同时考虑了重投影一致性和空间支持。

**关键创新**：Geo6DPose的关键创新在于其几何滤波策略。通过将视觉特征与几何信息相结合，该方法能够有效地过滤掉错误的对应关系，从而提高姿态估计的准确性和鲁棒性。与现有方法相比，Geo6DPose不需要训练或微调，并且可以在本地设备上运行，从而更适用于实际的机器人应用。

**关键设计**：
* **DINO特征提取器**：使用预训练的DINO模型提取视觉特征，该模型具有良好的泛化能力。
* **几何一致性检验**：利用场景深度信息将2D特征点反投影到3D空间，并与物体模型的3D点进行匹配，过滤掉不一致的对应关系。
* **加权几何对齐度量**：设计了一种加权几何对齐度量，用于评估恢复姿态的质量，该度量同时考虑了重投影误差和空间支持。

## 📊 实验亮点

Geo6DPose在单个商用GPU上实现了亚秒级推理（1.08 FPS），同时达到了与显著更大的零样本基线相当的平均召回率（53.7 AR）。该方法不需要训练、微调或网络访问，并且与不断发展的基础骨干网络兼容，展示了其在实际机器人应用中的潜力。

## 🎯 应用场景

Geo6DPose适用于资源受限的机器人应用场景，例如仓储物流、家庭服务机器人和工业自动化。该方法无需训练和网络连接，降低了部署成本和风险，并提高了系统的可靠性。未来，Geo6DPose可以进一步扩展到更复杂的场景和物体，并与其他感知模块集成，从而实现更智能的机器人系统。

## 📄 摘要（原文）

> Recent progress in zero-shot 6D object pose estimation has been driven largely by large-scale models and cloud-based inference. However, these approaches often introduce high latency, elevated energy consumption, and deployment risks related to connectivity, cost, and data governance; factors that conflict with the practical constraints of real-world robotics, where compute is limited and on-device inference is frequently required. We introduce Geo6DPose, a lightweight, fully local, and training-free pipeline for zero-shot 6D pose estimation that trades model scale for geometric reliability. Our method combines foundation model visual features with a geometric filtering strategy: Similarity maps are computed between onboarded template DINO descriptors and scene patches, and mutual correspondences are established by projecting scene patch centers to 3D and template descriptors to the object model coordinate system. Final poses are recovered via correspondence-driven RANSAC and ranked using a weighted geometric alignment metric that jointly accounts for reprojection consistency and spatial support, improving robustness to noise, clutter, and partial visibility. Geo6DPose achieves sub-second inference on a single commodity GPU while matching the average recall of significantly larger zero-shot baselines (53.7 AR, 1.08 FPS). It requires no training, fine-tuning, or network access, and remains compatible with evolving foundation backbones, advancing practical, fully local 6D perception for robotic deployment.

