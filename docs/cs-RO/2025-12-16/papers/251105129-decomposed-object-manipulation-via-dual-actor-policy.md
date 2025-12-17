---
layout: default
title: Decomposed Object Manipulation via Dual-Actor Policy
---

# Decomposed Object Manipulation via Dual-Actor Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.05129" class="toolbar-btn" target="_blank">📄 arXiv: 2511.05129</a>
  <a href="https://arxiv.org/pdf/2511.05129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05129" onclick="toggleFavorite(this, '2511.05129', 'Decomposed Object Manipulation via Dual-Actor Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Fan, Jian-Jian Jiang, Zhuohao Li, Xiao-Ming Wu, Yi-Xiang He, YiHan Yang, Shengbang Liu, Wei-Shi Zheng

**分类**: cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出双Actor策略DAP，解决物体操作任务中不同阶段的策略学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `物体操作` `双Actor策略` `可供性` `运动流` `机器人学习`

## 📋 核心要点

1. 现有物体操作方法忽略了任务的阶段性，依赖单一策略学习整个过程，导致性能受限。
2. 提出双Actor策略DAP，利用可供性先验和运动流先验，分别优化接近和操作阶段。
3. 构建包含视觉先验的模拟数据集，实验表明DAP在多个场景下优于SOTA方法。

## 📝 摘要（中文）

本文提出了一种新颖的双Actor策略（DAP），显式地考虑了物体操作任务中的接近阶段和操作阶段，并利用异构视觉先验来增强每个阶段。具体来说，引入了一个基于可供性的Actor来定位操作任务中的功能部件，从而改进接近过程。随后，提出了一个基于运动流的Actor来捕获部件的运动，从而促进操作过程。最后，引入了一个决策器来确定DAP的当前阶段并选择相应的Actor。此外，现有的物体操作数据集包含的对象很少，并且缺乏支持训练所需的视觉先验。为了解决这个问题，构建了一个模拟数据集，即双先验物体操作数据集，该数据集结合了两种视觉先验，并包括七个任务，包括两个具有挑战性的长期多阶段任务。在我们的数据集、RoboTwin基准和真实场景中的实验结果表明，我们的方法始终优于SOTA方法，平均分别提高了5.55%、14.7%和10.4%。

## 🔬 方法详解

**问题定义**：物体操作任务通常包含接近和操作两个阶段，现有方法通常使用单一策略直接学习整个过程，忽略了任务的阶段性特点，难以有效利用不同阶段的视觉信息，导致操作性能受限。此外，现有数据集规模小，缺乏视觉先验，不利于策略学习。

**核心思路**：将物体操作任务分解为接近和操作两个阶段，并为每个阶段设计专门的Actor。接近阶段利用可供性先验定位功能部件，操作阶段利用运动流先验捕获部件运动。通过决策器动态选择合适的Actor，从而实现更高效的物体操作。

**技术框架**：DAP包含三个主要模块：基于可供性的Actor、基于运动流的Actor和决策器。基于可供性的Actor负责接近阶段，通过学习可供性特征定位功能部件。基于运动流的Actor负责操作阶段，通过学习运动流特征控制部件运动。决策器根据当前状态选择合适的Actor执行动作。

**关键创新**：DAP的核心创新在于将物体操作任务分解为两个阶段，并为每个阶段设计专门的Actor，从而能够更有效地利用视觉先验信息。此外，提出的双先验物体操作数据集为训练DAP提供了充足的数据支持。

**关键设计**：可供性Actor和运动流Actor的网络结构未知，损失函数未知。决策器的设计细节未知。数据集包含七个任务，包括两个具有挑战性的长期多阶段任务，具体任务内容未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.05129/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.05129/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.05129/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DAP在自建数据集上优于SOTA方法5.55%，在RoboTwin基准上优于14.7%，在真实场景中优于10.4%。这些结果验证了DAP在不同场景下的有效性，表明其能够显著提升物体操作的性能。

## 🎯 应用场景

该研究成果可应用于机器人自动化操作、智能制造、家庭服务机器人等领域。通过提升机器人对物体的操作能力，可以实现更高效、更智能的自动化生产线，以及更便捷的家庭服务。未来，该方法有望扩展到更复杂的物体操作任务和更广泛的应用场景。

## 📄 摘要（原文）

> Object manipulation, which focuses on learning to perform tasks on similar parts across different types of objects, can be divided into an approaching stage and a manipulation stage. However, previous works often ignore this characteristic of the task and rely on a single policy to directly learn the whole process of object manipulation. To address this problem, we propose a novel Dual-Actor Policy, termed DAP, which explicitly considers different stages and leverages heterogeneous visual priors to enhance each stage. Specifically, we introduce an affordance-based actor to locate the functional part in the manipulation task, thereby improving the approaching process. Following this, we propose a motion flow-based actor to capture the movement of the component, facilitating the manipulation process. Finally, we introduce a decision maker to determine the current stage of DAP and select the corresponding actor. Moreover, existing object manipulation datasets contain few objects and lack the visual priors needed to support training. To address this, we construct a simulated dataset, the Dual-Prior Object Manipulation Dataset, which combines the two visual priors and includes seven tasks, including two challenging long-term, multi-stage tasks. Experimental results on our dataset, the RoboTwin benchmark and real-world scenarios illustrate that our method consistently outperforms the SOTA method by 5.55%, 14.7% and 10.4% on average respectively.

