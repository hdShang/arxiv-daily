---
layout: default
title: Learning to Reason in 4D: Dynamic Spatial Understanding for Vision Language Models
---

# Learning to Reason in 4D: Dynamic Spatial Understanding for Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20557" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20557v1</a>
  <a href="https://arxiv.org/pdf/2512.20557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20557v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20557v1', 'Learning to Reason in 4D: Dynamic Spatial Understanding for Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengchao Zhou, Yuxin Chen, Yuying Ge, Wei Huang, Jiehong Lin, Ying Shan, Xiaojuan Qi

**分类**: cs.CV

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出DSR Suite和几何选择模块GSM，提升VLM在动态空间推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态空间推理` `视觉语言模型` `4D感知` `几何选择模块` `视频理解`

## 📋 核心要点

1. 现有VLM在动态空间推理方面存在不足，缺乏大规模4D感知的训练数据是主要瓶颈。
2. 提出DSR Suite，包含自动生成DSR问答对的流程，以及轻量级的几何选择模块GSM，用于将几何先验知识融入VLM。
3. 实验表明，将DSR-Train和GSM集成到Qwen2.5-VL-7B中，显著提升了其动态空间推理能力，同时保持了通用视频理解的性能。

## 📝 摘要（中文）

视觉语言模型(VLM)在通用理解方面表现出色，但在动态空间推理(DSR)方面仍然较弱，即推理3D空间中物体几何和关系随时间的演变，这主要是由于缺乏可扩展的4D感知训练资源。为了弥合数据集、基准和模型方面的差距，我们引入了DSR Suite。首先，我们提出了一个自动化的流程，从真实视频中生成用于DSR的多项选择问答对。通过利用现代视觉基础模型，该流程提取丰富的几何和运动信息，包括相机姿态、局部点云、物体掩码、方向和3D轨迹。这些几何线索使得构建用于学习的DSR-Train和进一步人工改进的用于评估的DSR-Bench成为可能。与之前的工作相比，我们的数据强调(i)真实视频来源，(ii)物体和场景级别的3D要求，(iii)视点转换，(iv)多物体交互，以及(v)细粒度的程序性答案。除了数据，我们提出了一个轻量级的几何选择模块(GSM)，以无缝地将几何先验知识集成到VLM中，该模块将问题语义浓缩，并从预训练的4D重建先验知识中提取问题相关的知识到一组紧凑的几何token中。这种有针对性的提取避免了用不相关的知识淹没模型。实验表明，将DSR-Train和GSM集成到Qwen2.5-VL-7B中显著增强了其动态空间推理能力，同时保持了在通用视频理解基准上的准确性。

## 🔬 方法详解

**问题定义**：现有视觉语言模型(VLM)在理解静态图像方面表现出色，但在理解和推理动态3D空间中的物体运动和关系变化方面存在不足。主要痛点在于缺乏大规模、高质量的4D感知训练数据，以及如何有效地将3D几何信息融入到VLM中。

**核心思路**：论文的核心思路是通过自动化的数据生成流程，构建大规模的DSR数据集，并设计一个轻量级的几何选择模块(GSM)，将问题相关的几何先验知识提取并融入到VLM中。这样既解决了数据稀缺的问题，又避免了用不相关的几何信息淹没模型。

**技术框架**：整体框架包含两个主要部分：DSR Suite和几何选择模块(GSM)。DSR Suite负责生成大规模的DSR-Train和DSR-Bench数据集，利用视觉基础模型提取视频中的几何和运动信息。GSM则负责将问题语义和4D重建先验知识融合，生成几何token，并输入到VLM中。

**关键创新**：论文的关键创新在于：1) 提出了一个自动化的流程，可以从真实视频中生成大规模的DSR问答对，解决了数据稀缺的问题。2) 设计了轻量级的几何选择模块(GSM)，可以有效地将几何先验知识融入到VLM中，避免了信息过载的问题。

**关键设计**：DSR Suite的数据生成流程依赖于视觉基础模型，例如用于提取相机姿态、点云、物体掩码和3D轨迹的模型。GSM模块的设计目标是轻量级，因此采用了一个简单的神经网络结构，用于选择和融合几何特征。损失函数的设计旨在鼓励模型学习到问题相关的几何信息，并抑制不相关信息的干扰。具体参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20557v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20557v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20557v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，将DSR-Train和GSM集成到Qwen2.5-VL-7B中，显著增强了其动态空间推理能力。在DSR-Bench数据集上，模型的性能得到了显著提升，同时在通用视频理解基准上保持了良好的性能。这表明该方法在提升动态空间推理能力的同时，没有牺牲模型的通用性。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、视频监控、增强现实等领域。通过提升VLM对动态空间的理解能力，可以使机器人在复杂环境中更好地感知、推理和行动。例如，机器人可以根据视频中的物体运动轨迹，预测未来的状态，从而做出更合理的决策。

## 📄 摘要（原文）

> Vision-language models (VLM) excel at general understanding yet remain weak at dynamic spatial reasoning (DSR), i.e., reasoning about the evolvement of object geometry and relationship in 3D space over time, largely due to the scarcity of scalable 4D-aware training resources. To bridge this gap across aspects of dataset, benchmark and model, we introduce DSR Suite. First, we propose an automated pipeline that generates multiple-choice question-answer pairs from in-the-wild videos for DSR. By leveraging modern vision foundation models, the pipeline extracts rich geometric and motion information, including camera poses, local point clouds, object masks, orientations, and 3D trajectories. These geometric cues enable the construction of DSR-Train for learning and further human-refined DSR-Bench for evaluation. Compared with previous works, our data emphasize (i) in-the-wild video sources, (ii) object- and scene-level 3D requirements, (iii) viewpoint transformations, (iv) multi-object interactions, and (v) fine-grained, procedural answers. Beyond data, we propose a lightweight Geometry Selection Module (GSM) to seamlessly integrate geometric priors into VLMs, which condenses question semantics and extracts question-relevant knowledge from pretrained 4D reconstruction priors into a compact set of geometry tokens. This targeted extraction avoids overwhelming the model with irrelevant knowledge. Experiments show that integrating DSR-Train and GSM into Qwen2.5-VL-7B significantly enhances its dynamic spatial reasoning capability, while maintaining accuracy on general video understanding benchmarks.

