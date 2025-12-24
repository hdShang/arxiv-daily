---
layout: default
title: "Learn to Swim: Data-Driven LSTM Hydrodynamic Model for Quadruped Robot Gait Optimization"
---

# Learn to Swim: Data-Driven LSTM Hydrodynamic Model for Quadruped Robot Gait Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03146" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03146v1</a>
  <a href="https://arxiv.org/pdf/2505.03146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03146v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03146v1', 'Learn to Swim: Data-Driven LSTM Hydrodynamic Model for Quadruped Robot Gait Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Han, Pengming Guo, Hao Chen, Weikun Li, Jingbo Ren, Naijun Liu, Ning Yang, Dixia Fan

**分类**: cs.RO, cs.LG

**发布日期**: 2025-05-06

**备注**: This work has been accepted for publication in the IEEE International Conference on Robotics and Automation (ICRA) 2025. The final version will be available in IEEE Xplore (DOI to be assigned upon publication)

**DOI**: [10.1109/ICRA55743.2025.11128080](https://doi.org/10.1109/ICRA55743.2025.11128080)

---

## 💡 一句话要点

**提出FED-LSTM模型以优化四足机器人水下游泳性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `水下机器人` `流体动力学` `长短期记忆网络` `数据驱动模型` `运动优化` `实验验证` `四足机器人`

## 📋 核心要点

1. 现有的流动预测方法多依赖经验公式，难以准确捕捉复杂的流体动力学特性，尤其是在动态环境中。
2. 论文提出的FED-LSTM模型通过深度学习技术，利用实验数据训练，能够更好地预测水下四足机器人的水动力。
3. 实验结果表明，FED-LSTM在直线游泳和转向优化中显著减少了偏转误差，提高了转弯效率，验证了其优越性。

## 📝 摘要（中文）

本文提出了一种基于长短期记忆网络的流体实验数据驱动模型（FED-LSTM），用于预测我们构建的水下四足机器人上的非稳态、非线性水动力。该模型在循环水槽和拖曳水槽中进行的腿部力和身体阻力测试的实验数据上训练，表现出优于传统的经验公式（EF）的流动预测能力。FED-LSTM在直线游泳和转向步态优化中展现出更高的准确性和适应性，减少了直线游泳中的偏转误差，并在不增加转弯半径的情况下提高了转弯时间。硬件实验进一步验证了该模型在精度和稳定性方面的优势，为提升四足机器人游泳性能提供了坚实的基础。

## 🔬 方法详解

**问题定义**：本文旨在解决传统经验公式在水下四足机器人流动预测中的不足，尤其是在复杂流体动力学环境下的准确性和适应性问题。

**核心思路**：通过构建基于长短期记忆网络的流体实验数据驱动模型（FED-LSTM），利用实验数据进行训练，从而提高对非稳态、非线性水动力的预测能力。

**技术框架**：模型的整体架构包括数据采集、模型训练和性能评估三个主要阶段。首先在循环水槽和拖曳水槽中进行实验数据采集，然后使用这些数据训练FED-LSTM模型，最后通过硬件实验验证模型的预测精度和稳定性。

**关键创新**：FED-LSTM模型的最大创新在于其能够有效捕捉复杂的流体动力学特性，超越了传统经验公式的局限性，尤其是在动态游泳场景下的表现。

**关键设计**：模型的设计包括特定的网络结构和损失函数设置，确保在训练过程中能够准确反映流体动力学的复杂性，具体参数设置和网络层次结构在论文中详细描述。

## 📊 实验亮点

实验结果显示，FED-LSTM模型在直线游泳中减少了偏转误差，并在转弯时提高了转弯效率，转弯时间显著缩短而转弯半径未增加。与传统经验公式相比，模型的精度和稳定性得到了显著提升，验证了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括水下机器人、海洋探测、救援任务等，能够显著提升四足机器人在水下环境中的运动性能。未来，FED-LSTM模型的成功应用可能推动更多智能机器人在复杂流体环境中的发展与应用。

## 📄 摘要（原文）

> This paper presents a Long Short-Term Memory network-based Fluid Experiment Data-Driven model (FED-LSTM) for predicting unsteady, nonlinear hydrodynamic forces on the underwater quadruped robot we constructed. Trained on experimental data from leg force and body drag tests conducted in both a recirculating water tank and a towing tank, FED-LSTM outperforms traditional Empirical Formulas (EF) commonly used for flow prediction over flat surfaces. The model demonstrates superior accuracy and adaptability in capturing complex fluid dynamics, particularly in straight-line and turning-gait optimizations via the NSGA-II algorithm. FED-LSTM reduces deflection errors during straight-line swimming and improves turn times without increasing the turning radius. Hardware experiments further validate the model's precision and stability over EF. This approach provides a robust framework for enhancing the swimming performance of legged robots, laying the groundwork for future advances in underwater robotic locomotion.

