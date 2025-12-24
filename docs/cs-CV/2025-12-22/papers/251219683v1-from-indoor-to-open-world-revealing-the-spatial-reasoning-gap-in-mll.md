---
layout: default
title: "From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs"
---

# From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19683" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19683v1</a>
  <a href="https://arxiv.org/pdf/2512.19683.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19683v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19683v1', 'From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingrui Wu, Zhaozhi Wang, Fangjinhua Wang, Jiaolong Yang, Marc Pollefeys, Tong Zhang

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Project page: https://harmlesssr.github.io/openbench/

---

## 💡 一句话要点

**揭示多模态大语言模型在开放世界空间推理方面的差距，并提出相应评测基准。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `空间推理` `开放世界` `评测基准` `视觉推理`

## 📋 核心要点

1. 现有多模态大语言模型在空间智能方面存在不足，尤其是在开放世界场景下，缺乏有效的评测基准。
2. 论文构建了一个大规模的、基于行人视角视频的开放世界空间推理基准，包含精确的3D信息和分层空间推理问题。
3. 实验表明，现有模型在开放世界中的性能显著下降，且过度依赖语言先验，缺乏真正的视觉推理能力。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在语义任务上取得了令人印象深刻的性能，但其空间智能——对于鲁棒和有基础的AI系统至关重要——仍然不发达。现有的基准测试无法诊断这种局限性：它们要么侧重于过于简化的定性推理，要么依赖于特定领域的室内数据，并受到缺乏具有可验证度量真值的室外数据集的限制。为了弥合这一差距，我们引入了一个大规模基准，该基准建立在用同步立体相机、激光雷达和IMU/GPS传感器捕获的行人视角视频之上。该数据集提供了度量上精确的3D信息，从而能够自动生成空间推理问题，这些问题跨越了从定性关系推理到定量度量和运动学理解的分层范围。评估表明，在结构化室内基准中观察到的性能增益在开放世界环境中消失了。使用合成异常场景和盲测的进一步分析证实，当前的MLLM严重依赖于语言先验而不是有基础的视觉推理。因此，我们的基准提供了一个原则性的平台，用于诊断这些局限性并推进物理基础的空间智能。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型在空间推理能力上存在不足，尤其是在从室内环境迁移到复杂的开放世界环境时。现有的评测基准要么过于简单，侧重于定性推理，要么依赖于特定领域的室内数据，缺乏具有精确度量真值的室外数据集，难以全面评估模型的空间智能。

**核心思路**：论文的核心思路是构建一个大规模、具有度量真值的开放世界空间推理基准，该基准基于行人视角的视频数据，包含丰富的3D信息，并能够自动生成涵盖不同层次空间推理能力的问题。通过在该基准上评估现有模型，揭示其在开放世界空间推理方面的差距，并促进相关研究。

**技术框架**：该基准的构建流程主要包括以下几个阶段：1) 数据采集：使用同步立体相机、激光雷达和IMU/GPS传感器采集行人视角的视频数据。2) 3D重建：利用采集到的数据进行精确的3D重建，生成具有度量真值的3D场景。3) 问题生成：自动生成涵盖不同层次空间推理能力的问题，包括定性关系推理、定量度量理解和运动学理解。4) 模型评估：使用生成的基准测试评估现有MLLM的空间推理能力。

**关键创新**：该论文的关键创新在于构建了一个大规模、具有度量真值的开放世界空间推理基准，该基准能够全面评估MLLM在复杂环境下的空间智能。与现有基准相比，该基准具有以下优势：1) 数据规模更大，场景更复杂；2) 具有精确的度量真值，能够进行定量评估；3) 涵盖不同层次的空间推理能力，能够更全面地评估模型的空间智能。

**关键设计**：该基准的关键设计包括：1) 使用行人视角的视频数据，更贴近实际应用场景；2) 使用同步立体相机、激光雷达和IMU/GPS传感器，保证3D重建的精度；3) 自动生成不同类型的空间推理问题，保证基准的多样性和覆盖性；4) 设计了合成异常场景和盲测，用于评估模型对语言先验的依赖程度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19683v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19683v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19683v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有MLLM在开放世界空间推理基准上的性能显著低于室内环境，验证了模型在开放世界场景下的空间智能不足。通过合成异常场景和盲测，进一步证实了现有模型过度依赖语言先验，缺乏真正的视觉推理能力。该基准的发布将促进相关研究，推动物理基础的空间智能发展。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、增强现实等领域。通过提升多模态大语言模型的空间推理能力，可以使机器人更好地理解和适应复杂环境，提高导航的准确性和鲁棒性。在自动驾驶领域，可以提高车辆对周围环境的感知和理解能力，从而提高驾驶安全性。在增强现实领域，可以实现更自然的虚拟物体与真实环境的交互。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have achieved impressive performance on semantic tasks, their spatial intelligence--crucial for robust and grounded AI systems--remains underdeveloped. Existing benchmarks fall short of diagnosing this limitation: they either focus on overly simplified qualitative reasoning or rely on domain-specific indoor data, constrained by the lack of outdoor datasets with verifiable metric ground truth. To bridge this gap, we introduce a large-scale benchmark built from pedestrian-perspective videos captured with synchronized stereo cameras, LiDAR, and IMU/GPS sensors. This dataset provides metrically precise 3D information, enabling the automatic generation of spatial reasoning questions that span a hierarchical spectrum--from qualitative relational reasoning to quantitative metric and kinematic understanding. Evaluations reveal that the performance gains observed in structured indoor benchmarks vanish in open-world settings. Further analysis using synthetic abnormal scenes and blinding tests confirms that current MLLMs depend heavily on linguistic priors instead of grounded visual reasoning. Our benchmark thus provides a principled platform for diagnosing these limitations and advancing physically grounded spatial intelligence.

