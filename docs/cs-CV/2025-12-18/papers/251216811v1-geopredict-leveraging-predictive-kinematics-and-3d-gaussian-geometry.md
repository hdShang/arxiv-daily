---
layout: default
title: GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation
---

# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16811" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16811v1</a>
  <a href="https://arxiv.org/pdf/2512.16811.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16811v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16811v1', 'GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingjing Qian, Boyao Han, Chen Shi, Lei Xiao, Long Yang, Shaoshuai Shi, Li Jiang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**GeoPredict：利用预测运动学和3D高斯几何实现精确的VLA操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人操作` `3D几何推理` `预测运动学` `3D高斯几何`

## 📋 核心要点

1. 现有VLA模型在精确3D操作任务中表现不足，主要原因是其反应式和2D中心的特性。
2. GeoPredict通过引入预测运动学和3D高斯几何先验，增强VLA模型的3D推理能力，提升操作精度。
3. 实验表明，GeoPredict在多个数据集和真实场景中，显著优于现有VLA基线，尤其在几何密集型任务中。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在机器人操作中表现出强大的泛化能力，但很大程度上是反应式的和以2D为中心的，这使得它们在需要精确3D推理的任务中不可靠。我们提出了GeoPredict，一个几何感知的VLA框架，它用预测运动学和几何先验来增强连续动作策略。GeoPredict引入了一个轨迹级模块，该模块编码运动历史并预测机器人手臂的多步3D关键点轨迹，以及一个预测性3D高斯几何模块，该模块预测工作空间几何形状，并通过沿未来关键点轨迹的跟踪引导细化。这些预测模块仅作为训练时的监督，通过基于深度的渲染实现，而推理只需要轻量级的额外查询token，无需调用任何3D解码。在RoboCasa Human-50、LIBERO和真实世界操作任务上的实验表明，GeoPredict始终优于强大的VLA基线，尤其是在几何密集型和空间要求高的场景中。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作(VLA)模型在机器人操作任务中，尤其是在需要精确3D推理的任务中，存在泛化能力不足的问题。这些模型通常是反应式的，即根据当前观察到的状态立即做出动作决策，缺乏对未来状态的预测和规划。此外，它们主要以2D视觉信息为基础，难以准确理解和利用3D几何信息，导致在几何密集型场景中表现不佳。

**核心思路**：GeoPredict的核心思路是利用预测性的运动学和几何先验来增强VLA模型的3D推理能力。通过预测机器人手臂的未来运动轨迹和工作空间的几何形状，模型可以更好地理解任务的3D空间结构，从而做出更精确的动作决策。这种预测性的方法使得模型能够提前规划，避免了反应式方法中的盲目性。

**技术框架**：GeoPredict框架包含一个轨迹级模块和一个预测性3D高斯几何模块。轨迹级模块编码运动历史，并预测机器人手臂的多步3D关键点轨迹。预测性3D高斯几何模块预测工作空间几何形状，并通过沿未来关键点轨迹的跟踪引导细化。这两个模块在训练时作为监督信号，通过深度渲染提供3D信息。在推理阶段，只需要额外的查询token，无需进行复杂的3D解码。

**关键创新**：GeoPredict的关键创新在于引入了预测性的运动学和几何先验，并将其作为训练时的监督信号。这种方法有效地利用了3D信息，提高了VLA模型在几何密集型任务中的性能。此外，GeoPredict在推理阶段避免了复杂的3D解码，保持了模型的轻量级和高效性。

**关键设计**：GeoPredict使用轨迹级模块预测机器人手臂的多步3D关键点轨迹，这需要设计合适的网络结构来编码运动历史并预测未来的关键点位置。预测性3D高斯几何模块使用3D高斯表示来建模工作空间的几何形状，并设计了跟踪引导细化机制，以提高几何预测的准确性。损失函数的设计需要平衡运动学预测和几何预测的准确性，并确保模型能够有效地利用这些预测信息来指导动作决策。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16811v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16811v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16811v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GeoPredict在RoboCasa Human-50、LIBERO和真实世界操作任务上进行了评估，实验结果表明，GeoPredict始终优于强大的VLA基线。尤其是在几何密集型和空间要求高的场景中，GeoPredict的性能提升更为显著，证明了其在精确3D操作方面的优势。

## 🎯 应用场景

GeoPredict在机器人操作领域具有广泛的应用前景，例如在复杂装配、精细操作、以及需要与不规则物体交互的场景中。该研究成果可以提升机器人在工业自动化、医疗机器人、家庭服务机器人等领域的智能化水平，使其能够更好地适应复杂多变的环境，完成更加精细和复杂的任务。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models achieve strong generalization in robotic manipulation but remain largely reactive and 2D-centric, making them unreliable in tasks that require precise 3D reasoning. We propose GeoPredict, a geometry-aware VLA framework that augments a continuous-action policy with predictive kinematic and geometric priors. GeoPredict introduces a trajectory-level module that encodes motion history and predicts multi-step 3D keypoint trajectories of robot arms, and a predictive 3D Gaussian geometry module that forecasts workspace geometry with track-guided refinement along future keypoint trajectories. These predictive modules serve exclusively as training-time supervision through depth-based rendering, while inference requires only lightweight additional query tokens without invoking any 3D decoding. Experiments on RoboCasa Human-50, LIBERO, and real-world manipulation tasks show that GeoPredict consistently outperforms strong VLA baselines, especially in geometry-intensive and spatially demanding scenarios.

