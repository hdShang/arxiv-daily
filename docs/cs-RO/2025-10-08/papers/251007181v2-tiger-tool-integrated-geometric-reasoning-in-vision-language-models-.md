---
layout: default
title: TIGeR: Tool-Integrated Geometric Reasoning in Vision-Language Models for Robotics
---

# TIGeR: Tool-Integrated Geometric Reasoning in Vision-Language Models for Robotics

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07181" target="_blank" class="toolbar-btn">arXiv: 2510.07181v2</a>
    <a href="https://arxiv.org/pdf/2510.07181.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07181v2" 
            onclick="toggleFavorite(this, '2510.07181v2', 'TIGeR: Tool-Integrated Geometric Reasoning in Vision-Language Models for Robotics')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yi Han, Cheng Chi, Enshen Zhou, Shanyu Rong, Jingkun An, Pengwei Wang, Zhongyuan Wang, Lu Sheng, Shanghang Zhang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-08 (更新: 2025-10-09)

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**TIGeR：通过工具集成几何推理，提升视觉-语言模型在机器人领域的精度**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉-语言模型` `机器人操作` `几何推理` `工具集成` `深度学习`

## 📋 核心要点

1. 现有视觉-语言模型在机器人几何推理中精度不足，无法满足厘米级操作需求，主要原因是缺乏对深度信息和相机参数的有效利用。
2. TIGeR的核心思想是让模型通过调用外部工具进行精确的几何计算，而非将复杂计算内置于神经网络中，从而提升精度。
3. TIGeR通过构建TIGeR-300K数据集和两阶段训练流程，在几何推理基准测试和真实机器人操作中均取得了显著的性能提升。

## 📝 摘要（中文）

视觉-语言模型(VLMs)在空间推理方面表现出卓越的能力，但本质上仍受限于定性精度，缺乏真实世界机器人所需的计算精度。现有方法未能利用深度传感器和相机校准提供的度量线索，而是将几何问题简化为模式识别任务，无法提供机器人操作所需的厘米级精度。我们提出了TIGeR（工具集成几何推理），这是一个新颖的框架，通过使VLMs能够生成和执行精确的几何计算，从而将VLMs从感知估计器转变为几何计算器。TIGeR不尝试将复杂的几何操作内置于神经网络中，而是使模型能够识别几何推理需求，合成适当的计算代码，并调用专门的库进行精确计算。为了支持这种范式，我们引入了TIGeR-300K，这是一个全面的、面向工具调用的数据集，涵盖点变换、姿态估计和空间兼容性验证，包含工具调用序列和中间计算。通过结合监督微调(SFT)和强化微调(RFT)的两阶段训练流程，以及我们提出的分层奖励设计，TIGeR在几何推理基准测试中实现了SOTA性能，并在真实世界的机器人操作任务中展示了厘米级的精度。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在机器人操作任务中，几何推理精度不足，无法满足实际应用需求。它们通常将几何问题视为模式识别，忽略了深度传感器和相机标定的度量信息，导致精度受限。

**核心思路**：TIGeR的核心思路是将视觉-语言模型从“感知估计器”转变为“几何计算器”。通过赋予模型调用外部工具的能力，使其能够生成并执行精确的几何计算，从而绕过神经网络内部复杂几何运算的限制，提高精度。

**技术框架**：TIGeR框架包含以下几个主要组成部分：1) 几何推理需求识别模块，用于判断是否需要进行几何计算；2) 代码生成模块，根据需求生成相应的计算代码；3) 工具调用模块，执行生成的代码，调用外部几何计算库；4) 结果整合模块，将计算结果整合到视觉-语言模型的输出中。训练过程采用两阶段策略：首先是监督微调(SFT)，然后是强化微调(RFT)。

**关键创新**：TIGeR的关键创新在于“工具集成”的思想。它打破了传统视觉-语言模型将所有功能都内置于神经网络中的模式，而是通过调用外部工具来完成复杂的几何计算。这种方法不仅提高了精度，还增强了模型的可解释性和可扩展性。此外，TIGeR-300K数据集的构建也为该方法提供了数据支撑。

**关键设计**：TIGeR-300K数据集包含点变换、姿态估计和空间兼容性验证等任务，每个任务都包含工具调用序列和中间计算结果。强化微调阶段采用了分层奖励设计，对模型的每一步操作都进行评估和奖励，从而引导模型学习正确的工具调用策略。具体的奖励函数设计细节未知。

## 📊 实验亮点

TIGeR在几何推理基准测试中取得了SOTA性能，并在真实世界的机器人操作任务中展示了厘米级的精度。具体性能数据未知，但论文强调了TIGeR在精度方面的显著提升，表明其在实际应用中具有很高的价值。与现有方法相比，TIGeR通过工具集成的方式，显著提高了几何推理的精度和可靠性。

## 🎯 应用场景

TIGeR具有广泛的应用前景，可应用于机器人操作、自动驾驶、增强现实等领域。例如，在机器人操作中，TIGeR可以帮助机器人更精确地抓取物体、进行装配等任务。在自动驾驶中，TIGeR可以提高车辆对周围环境的感知和理解能力，从而提高驾驶安全性。在增强现实中，TIGeR可以实现更逼真的虚拟物体与现实世界的交互。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have shown remarkable capabilities in spatial reasoning, yet they remain fundamentally limited to qualitative precision and lack the computational precision required for real-world robotics. Current approaches fail to leverage metric cues from depth sensors and camera calibration, instead reducing geometric problems to pattern recognition tasks that cannot deliver the centimeter-level accuracy essential for robotic manipulation. We present TIGeR (Tool-Integrated Geometric Reasoning), a novel framework that transforms VLMs from perceptual estimators to geometric computers by enabling them to generate and execute precise geometric computations through external tools. Rather than attempting to internalize complex geometric operations within neural networks, TIGeR empowers models to recognize geometric reasoning requirements, synthesize appropriate computational code, and invoke specialized libraries for exact calculations. To support this paradigm, we introduce TIGeR-300K, a comprehensive tool-invocation-oriented dataset covering point transformations, pose estimation, and spatial compatibility verification, complete with tool invocation sequences and intermediate computations. Through a two-stage training pipeline combining supervised fine-tuning (SFT) and reinforcement fine-tuning (RFT) with our proposed hierarchical reward design, TIGeR achieves SOTA performance on geometric reasoning benchmarks while demonstrating centimeter-level precision in real-world robotic manipulation tasks.

