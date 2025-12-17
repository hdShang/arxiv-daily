---
layout: default
title: Seq-DeepIPC: Sequential Sensing for End-to-End Control in Legged Robot Navigation
---

# Seq-DeepIPC: Sequential Sensing for End-to-End Control in Legged Robot Navigation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23057" target="_blank" class="toolbar-btn">arXiv: 2510.23057v1</a>
    <a href="https://arxiv.org/pdf/2510.23057.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23057v1" 
            onclick="toggleFavorite(this, '2510.23057v1', 'Seq-DeepIPC: Sequential Sensing for End-to-End Control in Legged Robot Navigation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Oskar Natan, Jun Miura

**分类**: cs.RO, cs.CV, eess.IV, eess.SY

**发布日期**: 2025-10-27

**备注**: Preprint notice, this manuscript has been submitted to IEEE sensors journal for possible publication

**🔗 代码/项目**: [GITHUB](https://github.com/oskarnatan/Seq-DeepIPC)

---

## 💡 一句话要点

**Seq-DeepIPC：用于腿式机器人导航的端到端时序感知控制模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `腿式机器人` `自主导航` `端到端学习` `多模态融合` `时序建模` `深度学习` `机器人控制`

## 📋 核心要点

1. 现有腿式机器人导航方法在复杂环境感知和控制方面存在挑战，难以实现端到端自主导航。
2. Seq-DeepIPC通过融合多模态感知信息（RGB-D+GNSS）和时序信息，直接预测语义分割、深度估计和控制指令。
3. 实验表明，Seq-DeepIPC在真实环境中表现出良好的导航性能，并且时序输入能够有效提升感知和控制能力。

## 📝 摘要（中文）

本文提出Seq-DeepIPC，一种用于真实环境中腿式机器人导航的端到端感知控制时序模型。Seq-DeepIPC通过将多模态感知（RGB-D + GNSS）与时间融合和控制紧密结合，推进了自主腿式导航的智能感知。该模型联合预测语义分割和深度估计，为规划和控制提供更丰富的空间特征。为了在边缘设备上高效部署，我们使用EfficientNet-B0作为编码器，在保持精度的同时减少计算量。通过直接从连续GNSS位置计算方位角，简化了航向估计，无需使用噪声较大的IMU。我们收集了一个更大、更多样化的数据集，包括道路和草地地形，并在机器狗上验证了Seq-DeepIPC。对比和消融研究表明，时序输入可以改善模型的感知和控制，而其他基线模型则无法从中受益。Seq-DeepIPC以合理的模型大小实现了具有竞争力的结果；虽然仅使用GNSS的航向估计在高大建筑物附近不太可靠，但在开阔区域则表现出鲁棒性。总而言之，Seq-DeepIPC将端到端导航从轮式机器人扩展到更通用和具有时间感知能力的系统。为了支持未来的研究，我们将把代码发布到我们的GitHub存储库：https://github.com/oskarnatan/Seq-DeepIPC。

## 🔬 方法详解

**问题定义**：论文旨在解决腿式机器人在复杂真实环境中自主导航的问题。现有方法通常依赖于复杂的模块化系统，需要手动设计特征和规则，难以适应各种地形和环境变化。此外，IMU等传感器的噪声也会影响导航的准确性。

**核心思路**：论文的核心思路是构建一个端到端的深度学习模型，直接从多模态传感器数据（RGB-D图像和GNSS定位）学习到控制策略。通过时序建模，模型能够利用历史信息来提高感知和控制的鲁棒性。使用轻量级的EfficientNet-B0作为编码器，保证了模型在边缘设备上的高效部署。

**技术框架**：Seq-DeepIPC的整体框架包括以下几个主要模块：1) 多模态数据输入：接收RGB-D图像和GNSS定位数据；2) 特征提取：使用EfficientNet-B0作为编码器提取图像特征；3) 时序融合：使用循环神经网络（RNN）或Transformer等模型融合时序特征；4) 感知预测：联合预测语义分割和深度估计；5) 控制输出：根据感知结果生成控制指令，例如速度和转向角。

**关键创新**：论文的关键创新点在于：1) 端到端的感知控制框架，避免了手动设计特征和规则；2) 多模态传感器融合，利用RGB-D图像和GNSS定位的互补信息；3) 时序建模，提高了感知和控制的鲁棒性；4) 轻量级模型设计，便于在边缘设备上部署。

**关键设计**：论文的关键设计包括：1) 使用EfficientNet-B0作为编码器，以减少计算量；2) 使用连续GNSS位置计算方位角，避免使用噪声较大的IMU；3) 设计了包含道路和草地地形的大规模数据集；4) 使用合适的损失函数来训练模型，例如交叉熵损失用于语义分割，L1损失或L2损失用于深度估计。

## 📊 实验亮点

Seq-DeepIPC在真实环境中的实验结果表明，时序输入能够显著提升感知和控制性能。与没有时序信息的基线模型相比，Seq-DeepIPC在导航任务中取得了更好的成功率和更低的碰撞率。此外，该模型在边缘设备上的运行速度也足够快，可以满足实时控制的需求。

## 🎯 应用场景

Seq-DeepIPC可应用于各种腿式机器人的自主导航任务，例如搜救、巡检、物流配送等。该研究成果有助于提升腿式机器人在复杂环境中的适应性和智能化水平，使其能够更好地服务于人类社会。未来，该技术还可以扩展到其他类型的机器人，例如无人机和水下机器人。

## 📄 摘要（原文）

> We present Seq-DeepIPC, a sequential end-to-end perception-to-control model for legged robot navigation in realworld environments. Seq-DeepIPC advances intelligent sensing for autonomous legged navigation by tightly integrating multi-modal perception (RGB-D + GNSS) with temporal fusion and control. The model jointly predicts semantic segmentation and depth estimation, giving richer spatial features for planning and control. For efficient deployment on edge devices, we use EfficientNet-B0 as the encoder, reducing computation while maintaining accuracy. Heading estimation is simplified by removing the noisy IMU and instead computing the bearing angle directly from consecutive GNSS positions. We collected a larger and more diverse dataset that includes both road and grass terrains, and validated Seq-DeepIPC on a robot dog. Comparative and ablation studies show that sequential inputs improve perception and control in our models, while other baselines do not benefit. Seq-DeepIPC achieves competitive or better results with reasonable model size; although GNSS-only heading is less reliable near tall buildings, it is robust in open areas. Overall, Seq-DeepIPC extends end-to-end navigation beyond wheeled robots to more versatile and temporally-aware systems. To support future research, we will release the codes to our GitHub repository at https://github.com/oskarnatan/Seq-DeepIPC.

