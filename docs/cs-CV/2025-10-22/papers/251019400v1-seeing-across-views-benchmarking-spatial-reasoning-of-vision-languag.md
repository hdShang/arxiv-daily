---
layout: default
title: Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes
---

# Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.19400" target="_blank" class="toolbar-btn">arXiv: 2510.19400v1</a>
    <a href="https://arxiv.org/pdf/2510.19400.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19400v1" 
            onclick="toggleFavorite(this, '2510.19400v1', 'Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhiyuan Feng, Zhaolu Kang, Qijie Wang, Zhiying Du, Jiongrui Yan, Shubin Shi, Chengbo Yuan, Huizhi Liang, Yu Deng, Qixiu Li, Rushuai Yang, Arctanx An, Leqi Zheng, Weijie Wang, Shawn Chen, Sicheng Xu, Yaobo Liang, Jiaolong Yang, Baining Guo

**分类**: cs.CV

**发布日期**: 2025-10-22

**备注**: The project and benchmark are publicly available at https://github.com/microsoft/MV-RoboBench

---

## 💡 一句话要点

**提出MV-RoboBench基准，评估视觉-语言模型在机器人场景中的多视角空间推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `多视角学习` `机器人操作` `空间推理` `基准数据集`

## 📋 核心要点

1. 现有视觉-语言模型在机器人应用中缺乏对多视角信息的有效利用，尤其是在遮挡和深度模糊等问题上。
2. 提出MV-RoboBench基准，包含1.7k个QA项目，涵盖空间理解和机器人执行两大类，共八个子任务，用于评估多视角空间推理能力。
3. 实验结果表明，现有VLMs在多视角机器人感知方面仍有很大提升空间，且单视角基准上的优异性能不能保证在机器人任务中的成功。

## 📝 摘要（中文）

视觉-语言模型(VLMs)对于具身智能至关重要，使机器人能够在复杂环境中感知、推理和行动。它们也是最近的视觉-语言-动作(VLA)模型的基础。然而，大多数VLMs的评估都集中在单视角设置上，对其整合多视角信息的能力探索不足。同时，多摄像头设置在机器人平台中越来越普遍，因为它们提供了互补的视角来减轻遮挡和深度模糊。VLMs是否能有效地利用这种多视角输入进行机器人推理仍然是一个悬而未决的问题。为了弥合这一差距，我们引入了MV-RoboBench，这是一个专门用于评估VLMs在机器人操作中多视角空间推理能力的基准。MV-RoboBench包含1.7k个手动策划的QA项目，跨越八个子任务，分为两个主要类别：空间理解和机器人执行。我们评估了各种现有的VLMs，包括开源和闭源模型，以及结合了CoT启发技术的增强版本。结果表明，最先进的模型仍然远低于人类的表现，突显了VLMs在多视角机器人感知方面面临的巨大挑战。此外，我们的分析揭示了两个关键发现：(i)空间智能和机器人任务执行在多视角机器人场景中呈正相关；(ii)在现有通用单视角空间理解基准上的出色表现并不能可靠地转化为在我们的基准评估的机器人空间任务中的成功。我们发布MV-RoboBench作为一个开放资源，以促进空间定位的VLMs和VLAs的进展，不仅提供数据，还提供了一个用于多视角具身推理的标准化评估协议。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型在机器人场景下，如何有效利用多视角信息进行空间推理的问题。现有方法主要集中于单视角评估，忽略了多视角信息融合的重要性，导致模型在实际机器人应用中性能受限，尤其是在存在遮挡和深度歧义的情况下。

**核心思路**：论文的核心思路是构建一个专门用于评估多视角空间推理能力的基准数据集MV-RoboBench。通过设计包含空间理解和机器人执行任务的QA对，系统性地测试VLMs在多视角场景下的表现，从而推动相关研究的发展。

**技术框架**：MV-RoboBench基准包含以下几个关键组成部分：
1.  **场景构建**：模拟真实的机器人操作环境，使用多摄像头获取不同视角的图像。
2.  **任务设计**：设计八个子任务，涵盖空间理解（例如，物体定位、关系推理）和机器人执行（例如，抓取、放置）。
3.  **QA生成**：手动标注高质量的问答对，确保问题具有挑战性，答案需要模型进行多视角信息融合和空间推理。
4.  **评估指标**：采用准确率等指标，评估模型在不同任务上的表现。

**关键创新**：该论文的关键创新在于构建了一个专门针对多视角机器人场景的视觉-语言推理基准。与现有单视角基准相比，MV-RoboBench更贴近实际应用，能够更有效地评估VLMs在机器人任务中的潜力。此外，论文还分析了空间智能和机器人任务执行之间的相关性，以及单视角性能与多视角性能之间的差异，为未来的研究提供了有价值的见解。

**关键设计**：MV-RoboBench的数据集包含1.7k个手动标注的QA项目，涵盖了八个子任务。这些子任务的设计考虑了机器人操作的典型场景和挑战，例如，需要模型理解物体之间的空间关系、判断物体的可操作性、以及规划机器人的运动轨迹。论文还提供了一个标准化的评估协议，方便研究人员进行模型比较和性能分析。

## 📊 实验亮点

实验结果表明，现有最先进的VLMs在MV-RoboBench上的表现远低于人类水平，突显了多视角机器人感知的挑战性。研究还发现，在通用单视角空间理解基准上表现良好的模型，在MV-RoboBench上的表现并不一定出色，表明多视角机器人任务需要专门的模型设计和训练。

## 🎯 应用场景

该研究成果可应用于提升机器人在复杂环境中的感知和操作能力，例如智能仓储、自动驾驶、家庭服务机器人等领域。通过提高机器人对多视角信息的理解和推理能力，可以使其更好地完成各种任务，例如物体识别、导航、操作等，从而提高工作效率和安全性。

## 📄 摘要（原文）

> Vision-language models (VLMs) are essential to Embodied AI, enabling robots to perceive, reason, and act in complex environments. They also serve as the foundation for the recent Vision-Language-Action (VLA) models. Yet most evaluations of VLMs focus on single-view settings, leaving their ability to integrate multi-view information underexplored. At the same time, multi-camera setups are increasingly standard in robotic platforms, as they provide complementary perspectives to mitigate occlusion and depth ambiguity. Whether VLMs can effectively leverage such multi-view inputs for robotic reasoning therefore remains an open question. To bridge this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate the multi-view spatial reasoning capabilities of VLMs in robotic manipulation. MV-RoboBench consists of 1.7k manually curated QA items across eight subtasks, divided into two primary categories: spatial understanding and robotic execution. We evaluate a diverse set of existing VLMs, including both open-source and closed-source models, along with enhanced versions incorporating CoT-inspired techniques. The results show that state-of-the-art models remain far below human performance, underscoring the substantial challenges VLMs face in multi-view robotic perception. Additionally, our analysis uncovers two key findings: (i) spatial intelligence and robotic task execution are positively correlated in multi-view robotic scenarios; and (ii) strong performance on existing general-purpose single-view spatial understanding benchmarks does not reliably translate to success in the robotic spatial tasks assessed by our benchmark. We release MV-RoboBench as an open resource to foster progress in spatially grounded VLMs and VLAs, providing not only data but also a standardized evaluation protocol for multi-view embodied reasoning.

