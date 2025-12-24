---
layout: default
title: "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"
---

# Leave No Observation Behind: Real-time Correction for VLA Action Chunks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23224" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23224v1</a>
  <a href="https://arxiv.org/pdf/2509.23224.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23224v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23224v1', 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kohei Sendai, Maxime Alvarez, Tatsuya Matsushima, Yutaka Matsuo, Yusuke Iwasawa

**分类**: cs.RO, cs.AI, cs.CV, eess.SY

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出A2C2实时修正VLA模型动作块，提升长时序任务的反应性和鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `动作块` `实时控制` `异步校正` `长时程规划`

## 📋 核心要点

1. VLA模型通过预测动作块来提升效率，但会降低在延迟和长时程任务中的实时反应性。
2. A2C2通过轻量级的实时修正头，在每个控制步骤对VLA模型预测的动作块进行时间感知的修正。
3. 实验表明，A2C2在动态Kinetix和LIBERO Spatial任务中，显著提升了成功率和鲁棒性，且开销很小。

## 📝 摘要（中文）

为了提高效率和时间连贯性，视觉-语言-动作（VLA）模型通常预测动作块；然而，这种动作分块会损害推理延迟和长时程下的反应性。我们引入了异步动作块校正（A2C2），这是一个轻量级的实时块校正头，它在每个控制步骤运行，并将时间感知的校正添加到任何现成的VLA的动作块中。该模块结合了最新的观察、来自VLA的预测动作（基础动作）、编码基础动作在块内的索引的位置特征，以及来自基础策略的一些特征，然后输出每步校正。这保留了基础模型的能力，同时恢复了闭环响应性。该方法不需要重新训练基础策略，并且与诸如实时分块（RTC）之类的异步执行方案正交。在动态Kinetix任务套件（12个任务）和LIBERO Spatial上，我们的方法在增加延迟和执行范围的情况下，产生了持续的成功率提升（分别比RTC高+23%和+7%），并且即使在零注入延迟的情况下，也提高了长时程的鲁棒性。由于校正头很小且速度很快，因此与大型VLA模型的推理相比，开销很小。这些结果表明，A2C2是一种有效的插件机制，用于在实时控制中部署高容量分块策略。

## 🔬 方法详解

**问题定义**：VLA模型为了提高效率，通常会预测动作块，即一次性预测多个时间步的动作。然而，这种做法在实际应用中会引入延迟，尤其是在需要实时反馈和长时程规划的任务中，导致模型反应迟缓，性能下降。现有方法难以兼顾效率和实时性。

**核心思路**：A2C2的核心思想是在VLA模型预测的动作块的基础上，增加一个轻量级的校正模块，该模块在每个控制步骤运行，根据当前观测和动作块的信息，对动作进行实时修正。这样既保留了VLA模型的高效性，又提升了其在实时环境中的反应能力。

**技术框架**：A2C2作为一个独立的模块，可以插入到任何现有的VLA模型中。其输入包括：1) 当前时刻的观测；2) VLA模型预测的动作块（基础动作）；3) 位置特征，用于编码当前动作在动作块中的位置；4) 来自基础策略的一些特征。A2C2模块通过一个小型神经网络，输出一个动作修正量，该修正量被加到基础动作上，得到最终的控制动作。

**关键创新**：A2C2的关键创新在于其异步校正机制，它允许在不重新训练基础VLA模型的情况下，提升其在实时环境中的性能。此外，A2C2的设计轻量级，计算开销小，可以方便地部署在实际系统中。A2C2与现有的异步执行方案（如RTC）正交，可以结合使用以获得更好的效果。

**关键设计**：A2C2模块使用一个小型神经网络来实现，该网络可以采用全连接网络或卷积神经网络等结构。位置特征可以使用one-hot编码或嵌入向量来表示。损失函数通常采用均方误差损失，用于最小化修正后的动作与真实动作之间的差异。A2C2模块的训练可以采用监督学习或强化学习方法。

## 📊 实验亮点

在Kinetix任务套件和LIBERO Spatial数据集上的实验结果表明，A2C2能够显著提升VLA模型的性能。与RTC相比，A2C2在Kinetix任务套件上提升了23%的成功率，在LIBERO Spatial数据集上提升了7%的成功率。即使在零延迟的情况下，A2C2也能提高长时程任务的鲁棒性。此外，A2C2的计算开销很小，可以忽略不计。

## 🎯 应用场景

A2C2可广泛应用于需要实时控制和长时程规划的机器人任务中，例如自动驾驶、无人机控制、机器人操作等。通过提升VLA模型在这些场景下的反应性和鲁棒性，A2C2可以提高机器人的自主性和安全性，使其能够更好地适应复杂和动态的环境。

## 📄 摘要（原文）

> To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. We introduce Asynchronous Action Chunk Correction (A2C2), which is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction. This preserves the base model's competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC). On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, our method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay. Since the correction head is small and fast, there is minimal overhead compared to the inference of large VLA models. These results indicate that A2C2 is an effective, plug-in mechanism for deploying high-capacity chunking policies in real-time control.

