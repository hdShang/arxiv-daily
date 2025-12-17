---
layout: default
title: Evaluating the Performance of Deep Learning Models in Whole-body Dynamic 3D Posture Prediction During Load-reaching Activities
---

# Evaluating the Performance of Deep Learning Models in Whole-body Dynamic 3D Posture Prediction During Load-reaching Activities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20615" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20615v1</a>
  <a href="https://arxiv.org/pdf/2511.20615.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20615v1" onclick="toggleFavorite(this, '2511.20615v1', 'Evaluating the Performance of Deep Learning Models in Whole-body Dynamic 3D Posture Prediction During Load-reaching Activities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seyede Niloofar Hosseini, Ali Mojibi, Mahdi Mohseni, Navid Arjmand, Alireza Taheri

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-25

**备注**: 10 pages, 6 figures, 7 tables

---

## 💡 一句话要点

**提出基于Transformer的深度学习模型，用于预测负重活动中全身动态3D姿态。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `姿态预测` `深度学习` `时间序列模型` `Transformer` `BLSTM` `负重活动` `人体运动分析`

## 📋 核心要点

1. 现有方法难以准确预测动态负重活动中人体全身姿态，尤其是在长时间序列预测中。
2. 利用BLSTM和Transformer构建时间序列模型，并提出新的代价函数来约束身体节段长度，提高预测精度。
3. 实验结果表明，Transformer模型在长期预测中优于BLSTM，且提出的代价函数能有效降低预测误差。

## 📝 摘要（中文）

本研究旨在探索深度神经网络在动态负重活动中全身人体姿态预测的应用。使用双向长短期记忆网络(BLSTM)和Transformer架构训练了两个时间序列模型。数据集包含20名体重正常的健康男性个体在不同负重位置执行204个负重任务时的3D全身步态动态坐标，参与者采用了不同的搬运技术（包括弯腰、全蹲和半蹲，以及单手和双手）。模型输入包括手部负重位置的3D坐标、搬运技术、体重和身高，以及任务前25%时长的身体姿态3D坐标数据。模型使用这些输入来预测任务剩余75%时长的身体坐标。此外，提出了一种新方法，通过优化新的代价函数来强制执行恒定的身体节段长度，从而提高先前和当前姿态预测网络的准确性。结果表明，新的代价函数使手臂和腿部模型的预测误差分别降低了约8%和21%。Transformer架构的均方根误差为47.0毫米，比基于BLSTM的模型具有约58%的更准确的长期性能。本研究证明了利用神经网络捕获3D运动帧中的时间序列依赖性的价值，为理解和预测人工物料搬运活动中的运动动力学提供了一种独特的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决动态负重活动中，如何准确预测人体全身3D姿态的问题。现有方法在处理长时间序列依赖和保持身体结构一致性方面存在不足，导致预测精度不高。

**核心思路**：论文的核心思路是利用深度学习模型（BLSTM和Transformer）捕获运动过程中的时间序列依赖关系，并通过引入新的代价函数来约束身体节段长度，从而提高预测精度和保持身体结构的合理性。

**技术框架**：整体框架包括数据采集、模型训练和姿态预测三个主要阶段。首先，采集人体在进行负重活动时的3D全身姿态数据。然后，使用BLSTM和Transformer两种时间序列模型进行训练，模型的输入包括手部负重位置、搬运技术、体重身高以及任务前25%的身体姿态数据，输出为任务剩余75%的身体姿态数据。最后，通过优化代价函数来提高预测精度。

**关键创新**：最重要的技术创新点在于提出了一个新的代价函数，该函数通过约束身体节段长度的恒定性，来提高姿态预测的准确性和合理性。与传统方法相比，该方法能够更好地保持身体结构的完整性，避免出现不自然的姿态。

**关键设计**：代价函数的设计是关键。它惩罚预测姿态中身体节段长度的变化，从而鼓励模型生成更符合生物力学的姿态。此外，Transformer模型的结构和参数设置，以及BLSTM模型的层数和隐藏单元数等，都是影响模型性能的关键因素。论文中使用了均方根误差（RMSE）作为评估指标，并对模型进行了充分的训练和调优。

## 📊 实验亮点

实验结果表明，Transformer模型在长期姿态预测方面优于BLSTM模型，均方根误差为47.0毫米，精度提升约58%。此外，提出的代价函数能够有效降低预测误差，手臂和腿部模型的预测误差分别降低了约8%和21%。这些结果验证了所提出方法的有效性。

## 🎯 应用场景

该研究成果可应用于人机协作、康复训练、运动分析和虚拟现实等领域。例如，在人机协作中，机器人可以预测工人的姿态，从而更好地配合工人完成任务，降低工伤风险。在康复训练中，可以评估患者的运动能力，并提供个性化的训练方案。在运动分析中，可以分析运动员的动作，提高运动表现。在虚拟现实中，可以创建更逼真的人体运动模型。

## 📄 摘要（原文）

> This study aimed to explore the application of deep neural networks for whole-body human posture prediction during dynamic load-reaching activities. Two time-series models were trained using bidirectional long short-term memory (BLSTM) and transformer architectures. The dataset consisted of 3D full-body plug-in gait dynamic coordinates from 20 normal-weight healthy male individuals each performing 204 load-reaching tasks from different load positions while adapting various lifting and handling techniques. The model inputs consisted of the 3D position of the hand-load position, lifting (stoop, full-squat and semi-squat) and handling (one- and two-handed) techniques, body weight and height, and the 3D coordinate data of the body posture from the first 25% of the task duration. These inputs were used by the models to predict body coordinates during the remaining 75% of the task period. Moreover, a novel method was proposed to improve the accuracy of the previous and present posture prediction networks by enforcing constant body segment lengths through the optimization of a new cost function. The results indicated that the new cost function decreased the prediction error of the models by approximately 8% and 21% for the arm and leg models, respectively. We indicated that utilizing the transformer architecture, with a root-mean-square-error of 47.0 mm, exhibited ~58% more accurate long-term performance than the BLSTM-based model. This study merits the use of neural networks that capture time series dependencies in 3D motion frames, providing a unique approach for understanding and predict motion dynamics during manual material handling activities.

