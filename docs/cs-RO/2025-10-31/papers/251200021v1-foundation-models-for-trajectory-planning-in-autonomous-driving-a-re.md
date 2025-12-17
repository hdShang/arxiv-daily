---
layout: default
title: Foundation Models for Trajectory Planning in Autonomous Driving: A Review of Progress and Open Challenges
---

# Foundation Models for Trajectory Planning in Autonomous Driving: A Review of Progress and Open Challenges

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.00021" target="_blank" class="toolbar-btn">arXiv: 2512.00021v1</a>
    <a href="https://arxiv.org/pdf/2512.00021.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00021v1" 
            onclick="toggleFavorite(this, '2512.00021v1', 'Foundation Models for Trajectory Planning in Autonomous Driving: A Review of Progress and Open Challenges')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kemal Oksuz, Alexandru Buburuzan, Anthony Knittel, Yuhan Yao, Puneet K. Dokania

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-31

**备注**: Under review

**🔗 代码/项目**: [GITHUB](https://github.com/fiveai/FMs-for-driving-trajectories)

---

## 💡 一句话要点

**综述：自动驾驶轨迹规划中的Foundation Model进展与挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `轨迹规划` `Foundation Model` `多模态学习` `视觉-语言-动作模型`

## 📋 核心要点

1. 现有自动驾驶轨迹规划方法依赖手工设计，泛化能力弱，难以处理复杂场景。
2. 论文综述了基于Foundation Model的轨迹规划方法，利用多模态输入直接预测轨迹。
3. 论文分析了37种方法的架构、优缺点和开放性，并提供在线资源方便研究。

## 📝 摘要（中文）

多模态Foundation Model的出现显著改变了自动驾驶技术，使其从传统的手工设计转向统一的、基于Foundation Model的方法，能够直接从原始传感器输入推断运动轨迹。这类新方法还可以将自然语言作为额外的模态，其中视觉-语言-动作（VLA）模型是代表性例子。本综述通过统一的分类法，全面考察了这些方法，批判性地评估了它们的架构设计选择、方法优势以及固有的能力和局限性。我们的调查涵盖了37种最近提出的、涵盖了使用Foundation Model进行轨迹规划的方法。此外，我们还评估了这些方法在源代码和数据集方面的开放性，为从业者和研究人员提供了有价值的信息。我们提供了一个配套网页，根据我们的分类法对这些方法进行编目，网址为：https://github.com/fiveai/FMs-for-driving-trajectories

## 🔬 方法详解

**问题定义**：自动驾驶轨迹规划旨在根据环境感知信息生成安全、高效的车辆行驶轨迹。传统方法依赖于手工设计的规则和模块，难以适应复杂多变的交通环境，泛化能力受限。此外，传统方法通常难以有效融合多种模态的信息，例如视觉、激光雷达和自然语言指令。

**核心思路**：论文的核心思路是利用大规模预训练的Foundation Model，例如视觉-语言模型，直接从原始传感器数据（如图像、点云）和自然语言指令中学习轨迹规划策略。这种方法旨在通过端到端的方式，减少对人工特征工程的依赖，提高模型的泛化能力和适应性。

**技术框架**：基于Foundation Model的自动驾驶轨迹规划框架通常包含以下几个主要模块：1) 感知模块：负责从传感器数据中提取环境信息，例如车道线、交通标志、其他车辆等。2) 语言理解模块：负责解析自然语言指令，理解用户的意图。3) 轨迹生成模块：根据感知信息和语言指令，生成车辆的行驶轨迹。4) 控制模块：将生成的轨迹转化为车辆的控制指令，例如油门、刹车和方向盘角度。这些模块通常通过一个统一的Foundation Model进行端到端训练。

**关键创新**：该综述的关键创新在于对现有基于Foundation Model的轨迹规划方法进行了系统的分类和分析，提出了一个统一的分类法，并从架构设计、方法优势、能力和局限性等方面进行了深入的评估。此外，该综述还关注了这些方法的开放性，为研究人员和从业者提供了有价值的信息。

**关键设计**：不同的方法在关键设计上存在差异。例如，一些方法采用Transformer架构来融合多模态信息，另一些方法则采用循环神经网络来处理时序数据。损失函数的设计也至关重要，常见的损失函数包括轨迹预测误差、碰撞惩罚和舒适度指标。此外，数据增强技术也被广泛应用于提高模型的鲁棒性。

## 📊 实验亮点

该综述涵盖了37种基于Foundation Model的轨迹规划方法，并评估了它们在源代码和数据集方面的开放性。通过对比不同方法的性能和特点，为研究人员和从业者提供了选择合适方法的参考依据。该综述还指出了现有方法的局限性，为未来的研究方向提供了启示。

## 🎯 应用场景

该研究成果可应用于各种自动驾驶场景，包括城市道路、高速公路和停车场等。通过利用Foundation Model，可以提高自动驾驶系统的安全性、效率和舒适性，并支持更高级别的自动驾驶功能，例如根据自然语言指令进行导航和驾驶。

## 📄 摘要（原文）

> The emergence of multi-modal foundation models has markedly transformed the technology for autonomous driving, shifting away from conventional and mostly hand-crafted design choices towards unified, foundation-model-based approaches, capable of directly inferring motion trajectories from raw sensory inputs. This new class of methods can also incorporate natural language as an additional modality, with Vision-Language-Action (VLA) models serving as a representative example. In this review, we provide a comprehensive examination of such methods through a unifying taxonomy to critically evaluate their architectural design choices, methodological strengths, and their inherent capabilities and limitations. Our survey covers 37 recently proposed approaches that span the landscape of trajectory planning with foundation models. Furthermore, we assess these approaches with respect to the openness of their source code and datasets, offering valuable information to practitioners and researchers. We provide an accompanying webpage that catalogs the methods based on our taxonomy, available at: https://github.com/fiveai/FMs-for-driving-trajectories

