---
layout: default
title: BEAR: Benchmarking and Enhancing Multimodal Language Models for Atomic Embodied Capabilities
---

# BEAR: Benchmarking and Enhancing Multimodal Language Models for Atomic Embodied Capabilities

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08759" target="_blank" class="toolbar-btn">arXiv: 2510.08759v1</a>
    <a href="https://arxiv.org/pdf/2510.08759.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08759v1" 
            onclick="toggleFavorite(this, '2510.08759v1', 'BEAR: Benchmarking and Enhancing Multimodal Language Models for Atomic Embodied Capabilities')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yu Qi, Haibo Zhao, Ziyu Guo, Siyuan Ma, Ziyan Chen, Yaokun Han, Renrui Zhang, Zitiantao Lin, Shiji Xin, Yijian Huang, Kai Cheng, Peiheng Wang, Jiazheng Liu, Jiayi Zhang, Yizhe Zhu, Wenqing Wang, Yiran Qin, Xupeng Zhu, Haojie Huang, Lawson L. S. Wong

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**BEAR：原子具身能力的多模态语言模型基准测试与增强**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `具身智能` `基准测试` `视觉感知` `3D理解`

## 📋 核心要点

1. 现有具身智能体基准测试主要集中在特定领域，缺乏对多模态大语言模型原子具身能力的全面评估。
2. 论文提出BEAR基准测试，并设计BEAR-Agent，通过集成预训练视觉模型来增强MLLM的感知、3D理解和规划能力。
3. 实验结果表明，BEAR-Agent显著提升了MLLM在BEAR基准上的性能，并在模拟环境中验证了其有效性。

## 📝 摘要（中文）

具身能力是指智能体感知、理解和与物理世界交互的一系列基本能力。尽管多模态大型语言模型（MLLM）在具身智能体方面展现出潜力，但对其具身能力的全面和系统评估仍未充分探索，因为现有基准主要侧重于规划或空间理解等特定领域。为了弥合这一差距，我们推出了BEAR，这是一个全面的、细粒度的基准，用于评估MLLM在原子具身能力方面的表现。BEAR包含4469个交错的图像-视频-文本条目，涵盖6个类别中的14个领域，包括从低级指向、轨迹理解、空间推理到高级规划的任务。对20个代表性MLLM的广泛评估结果表明，它们在具身能力的各个领域都存在持续的局限性。为了解决这一不足，我们提出了BEAR-Agent，一种多模态可对话智能体，它集成了预训练的视觉模型，以增强MLLM的感知、3D理解和规划能力。它显著提高了MLLM在BEAR上各种具身能力上的性能，获得了9.12%的绝对增益和GPT-5上17.5%的相对改进。此外，我们的实验表明，提高MLLM的具身能力可以使模拟环境中的具身任务受益。

## 🔬 方法详解

**问题定义**：现有MLLM在具身智能体任务中表现出潜力，但缺乏一个全面细粒度的基准来评估其原子具身能力。现有基准测试往往只关注特定领域，如规划或空间理解，无法充分反映MLLM在感知、理解和交互方面的综合能力。因此，需要一个更全面的基准来揭示MLLM在具身能力方面的局限性，并指导模型改进。

**核心思路**：论文的核心思路是构建一个全面的基准测试BEAR，涵盖多种原子具身能力，并设计一个增强型智能体BEAR-Agent，通过集成预训练视觉模型来提升MLLM的感知、3D理解和规划能力。通过BEAR基准测试，可以系统地评估MLLM的性能瓶颈，并利用BEAR-Agent验证改进方法的有效性。

**技术框架**：BEAR-Agent的技术框架主要包括以下几个模块：1) 预训练视觉模型：用于增强MLLM的视觉感知能力，例如目标检测、语义分割等。2) 3D理解模块：用于提升MLLM对三维场景的理解能力，例如深度估计、场景重建等。3) 规划模块：用于增强MLLM的规划能力，例如路径规划、动作序列生成等。这些模块与MLLM进行集成，形成一个可对话的智能体。

**关键创新**：论文的关键创新在于：1) 提出了一个全面的原子具身能力基准测试BEAR，涵盖多个领域和任务。2) 设计了BEAR-Agent，通过集成预训练视觉模型来增强MLLM的感知、3D理解和规划能力。3) 实验结果表明，BEAR-Agent显著提升了MLLM在BEAR基准上的性能，并在模拟环境中验证了其有效性。

**关键设计**：BEAR基准测试的关键设计包括：1) 细粒度的任务划分，涵盖14个领域和6个类别。2) 多模态数据输入，包括图像、视频和文本。3) 多样化的评估指标，包括准确率、召回率、F1值等。BEAR-Agent的关键设计包括：1) 选择合适的预训练视觉模型，例如CLIP、DINO等。2) 设计有效的集成策略，将视觉模型与MLLM进行融合。3) 优化训练目标，使BEAR-Agent能够更好地完成具身任务。

## 📊 实验亮点

实验结果表明，BEAR-Agent在BEAR基准测试上取得了显著的性能提升，获得了9.12%的绝对增益和GPT-5上17.5%的相对改进。此外，实验还验证了提高MLLM的具身能力可以使模拟环境中的具身任务受益。这些结果表明，BEAR-Agent是一种有效的MLLM具身能力增强方法。

## 🎯 应用场景

该研究成果可应用于机器人、自动驾驶、虚拟现实等领域。通过提升MLLM的具身能力，可以使智能体更好地理解和与物理世界交互，从而实现更智能、更自主的应用。例如，在机器人领域，可以使机器人更好地完成导航、操作等任务；在自动驾驶领域，可以使车辆更好地感知和理解周围环境；在虚拟现实领域，可以使虚拟角色更逼真地与用户交互。

## 📄 摘要（原文）

> Embodied capabilities refer to a suite of fundamental abilities for an agent to perceive, comprehend, and interact with the physical world. While multimodal large language models (MLLMs) show promise as embodied agents, a thorough and systematic evaluation of their embodied capabilities remains underexplored, as existing benchmarks primarily focus on specific domains such as planning or spatial understanding. To bridge this gap, we introduce BEAR, a comprehensive and fine-grained benchmark that evaluates MLLMs on atomic embodied capabilities. BEAR comprises 4,469 interleaved image-video-text entries across 14 domains in 6 categories, including tasks from low-level pointing, trajectory understanding, spatial reasoning, to high-level planning. Extensive evaluation results of 20 representative MLLMs reveal their persistent limitations across all domains of embodied capabilities. To tackle the shortfall, we propose BEAR-Agent, a multimodal conversable agent that integrates pretrained vision models to strengthen MLLM perception, 3D understanding, and planning capabilities. It substantially enhances MLLM performance across diverse embodied capabilities on BEAR, yielding a 9.12% absolute gain and a relative improvement of 17.5% on GPT-5. Furthermore, our experiments indicate that improving MLLM embodied capabilities can benefit embodied tasks in simulated environments. Project website: https://bear-official66.github.io/

