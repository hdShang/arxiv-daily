---
layout: default
title: "GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation"
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

**关键词**: `视觉语言动作模型` `机器人操作` `3D几何推理` `运动学预测` `高斯混合模型`

## 📋 核心要点

1. 现有VLA模型在精确3D推理任务中表现不足，主要原因是其反应式和2D中心的设计。
2. GeoPredict通过预测运动学和几何先验增强VLA模型，提升其在复杂3D环境中的操作能力。
3. 实验表明，GeoPredict在多个数据集和真实场景中显著优于现有VLA基线，尤其是在几何相关的任务中。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在机器人操作中表现出强大的泛化能力，但很大程度上仍然是反应式的和以2D为中心的，这使得它们在需要精确3D推理的任务中不可靠。我们提出了GeoPredict，一个几何感知的VLA框架，它用预测运动学和几何先验来增强连续动作策略。GeoPredict引入了一个轨迹级模块，该模块编码运动历史并预测机器人手臂的多步3D关键点轨迹，以及一个预测性3D高斯几何模块，该模块预测工作空间几何形状，并通过沿未来关键点轨迹的跟踪引导细化。这些预测模块仅作为训练时的监督，通过基于深度的渲染实现，而推理只需要轻量级的额外查询token，无需调用任何3D解码。在RoboCasa Human-50、LIBERO和真实世界操作任务上的实验表明，GeoPredict始终优于强大的VLA基线，尤其是在几何密集型和空间要求高的场景中。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作(VLA)模型在机器人操作任务中，尤其是在需要精确3D推理的场景下，表现出局限性。这些模型通常是反应式的，依赖于当前观察到的图像信息来生成动作，缺乏对未来状态的预测能力，并且主要以2D为中心，难以准确理解和利用3D几何信息。这导致它们在几何密集型和空间要求高的任务中表现不佳。

**核心思路**：GeoPredict的核心思路是通过引入预测性的运动学和几何先验来增强VLA模型。具体来说，它预测机器人手臂未来多个步骤的3D关键点轨迹，并预测工作空间的3D几何形状。这些预测信息作为训练时的监督信号，引导模型学习更有效的3D表示和推理能力。在推理阶段，模型只需要轻量级的额外查询token，无需进行复杂的3D解码，从而保持了高效性。

**技术框架**：GeoPredict的整体框架包括一个连续动作策略网络，以及两个关键的预测模块：轨迹级模块和预测性3D高斯几何模块。轨迹级模块编码运动历史，并预测机器人手臂的多步3D关键点轨迹。预测性3D高斯几何模块预测工作空间的几何形状，并通过跟踪引导细化。这两个预测模块在训练时通过深度渲染提供监督信号，而在推理时仅需少量额外查询token。

**关键创新**：GeoPredict的关键创新在于将预测性的运动学和几何先验融入到VLA框架中。与传统的反应式VLA模型不同，GeoPredict能够预测未来的状态，从而更好地规划动作。此外，GeoPredict使用3D高斯几何来表示工作空间，并利用跟踪引导细化，从而提高了几何预测的准确性。最重要的是，这些预测模块只在训练时使用，推理时只需要轻量级的额外查询token，保证了推理效率。

**关键设计**：轨迹级模块使用Transformer网络来编码运动历史并预测3D关键点轨迹。预测性3D高斯几何模块使用3D高斯混合模型来表示工作空间的几何形状，并使用卡尔曼滤波等跟踪算法来引导几何预测的细化。损失函数包括轨迹预测损失和几何预测损失，通过深度渲染将预测的3D信息与真实深度图像进行比较，从而提供监督信号。推理时，通过额外的查询token将预测的运动学和几何信息融入到连续动作策略网络中。

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

GeoPredict在RoboCasa Human-50、LIBERO和真实世界操作任务上进行了评估，实验结果表明，GeoPredict始终优于强大的VLA基线。例如，在几何密集型和空间要求高的场景中，GeoPredict的性能提升显著。具体数据提升幅度在不同数据集和任务上有所不同，但总体上表明GeoPredict在精确3D操作方面具有显著优势。

## 🎯 应用场景

GeoPredict在机器人操作领域具有广泛的应用前景，例如在复杂环境下的物体抓取、装配、以及需要精确3D定位的任务中。该方法可以提升机器人在工业自动化、家庭服务、医疗辅助等领域的应用能力，使其能够更好地理解和操作周围环境，完成更加复杂和精细的任务。未来，该研究可以进一步扩展到更复杂的机器人系统和更广泛的应用场景。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models achieve strong generalization in robotic manipulation but remain largely reactive and 2D-centric, making them unreliable in tasks that require precise 3D reasoning. We propose GeoPredict, a geometry-aware VLA framework that augments a continuous-action policy with predictive kinematic and geometric priors. GeoPredict introduces a trajectory-level module that encodes motion history and predicts multi-step 3D keypoint trajectories of robot arms, and a predictive 3D Gaussian geometry module that forecasts workspace geometry with track-guided refinement along future keypoint trajectories. These predictive modules serve exclusively as training-time supervision through depth-based rendering, while inference requires only lightweight additional query tokens without invoking any 3D decoding. Experiments on RoboCasa Human-50, LIBERO, and real-world manipulation tasks show that GeoPredict consistently outperforms strong VLA baselines, especially in geometry-intensive and spatially demanding scenarios.

