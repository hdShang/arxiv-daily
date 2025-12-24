---
layout: default
title: PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation
---

# PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21652" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21652v3</a>
  <a href="https://arxiv.org/pdf/2505.21652.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21652v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21652v3', 'PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Yin, Zhengtao Han, Shivam Aarya, Jianxin Wang, Shuhang Xu, Jiawei Peng, Angtian Wang, Alan Yuille, Tianmin Shu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-06-16)

---

## 💡 一句话要点

**提出PartInstruct以解决细粒度机器人操控中的指令跟随问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细粒度操控` `部件级指令` `机器人学习` `3D模拟` `任务泛化`

## 📋 核心要点

1. 现有的机器人操控方法在细粒度任务中缺乏有效的部件级指令和数据集，导致操控精度不足。
2. 本文提出PartInstruct数据集，包含丰富的部件级信息和细粒度操控任务，旨在提升机器人对复杂任务的理解和执行能力。
3. 实验显示，当前的操控模型在部件概念的理解和长时间任务的执行上存在明显不足，亟需改进。

## 📝 摘要（中文）

细粒度机器人操控任务，如将瓶子旋转以展示标签，要求对物体部件及其与任务的关系进行稳健推理。尽管近期在基于语言指令的通用机器人操控策略训练上取得了进展，但缺乏大规模的细粒度操控任务数据集，尤其是带有部件级指令和多样化3D物体实例的标注。为此，本文提出了PartInstruct，这是第一个用于训练和评估细粒度机器人操控模型的基准数据集，包含513个物体实例和1302个细粒度操控任务。我们在3D模拟器中合成了超过10,000个专家演示，并设计了全面的测试套件以评估学习策略的泛化能力。实验结果表明，现有模型在部件概念的稳健性和3D空间动作预测上存在挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决细粒度机器人操控任务中缺乏部件级指令和大规模标注数据集的问题。现有方法在处理复杂任务时，往往无法有效理解物体部件及其关系，导致操控效果不佳。

**核心思路**：论文提出PartInstruct数据集，包含丰富的部件级信息和细粒度操控任务，通过提供高层任务指令和基于部件的技能指令，帮助机器人更好地理解和执行复杂操控任务。

**技术框架**：PartInstruct的整体架构包括数据集构建、专家演示合成和测试评估三个主要模块。数据集包含513个物体实例和1302个任务，演示通过3D模拟器生成，并与高层指令和部件信息配对。

**关键创新**：PartInstruct是第一个针对细粒度操控任务的部件级指令数据集，填补了现有研究的空白。与传统方法相比，它提供了更细致的任务指导，增强了模型的学习能力。

**关键设计**：在数据集构建中，采用了超过10,000个专家演示，并设计了全面的测试套件以评估模型的泛化能力。损失函数和网络结构的选择旨在提高模型对部件概念的理解和长时间任务的执行能力。

## 📊 实验亮点

实验结果表明，现有的机器人操控模型在PartInstruct基准上表现不佳，尤其是在部件概念的稳健性和长时间任务的执行上。具体而言，模型在3D空间中的动作预测准确率低于预期，显示出亟需改进的空间。

## 🎯 应用场景

该研究的潜在应用领域包括家庭服务机器人、工业自动化和医疗辅助机器人等。通过提升机器人对细粒度操控任务的理解能力，PartInstruct有望在实际应用中实现更高的灵活性和效率，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Fine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their relationships with intended tasks. Despite recent advances in training general-purpose robot manipulation policies guided by language instructions, there is a notable lack of large-scale datasets for fine-grained manipulation tasks with part-level instructions and diverse 3D object instances annotated with part-level labels. In this work, we introduce PartInstruct, the first large-scale benchmark for training and evaluating fine-grained robot manipulation models using part-level instructions. PartInstruct comprises 513 object instances across 14 categories, each annotated with part-level information, and 1302 fine-grained manipulation tasks organized into 16 task classes. Our training set consists of over 10,000 expert demonstrations synthesized in a 3D simulator, where each demonstration is paired with a high-level task instruction, a chain of base part-based skill instructions, and ground-truth 3D information about the object and its parts. Additionally, we designed a comprehensive test suite to evaluate the generalizability of learned policies across new states, objects, and tasks. We evaluated several state-of-the-art robot manipulation approaches, including end-to-end vision-language policy learning and bi-level planning models for robot manipulation on our benchmark. The experimental results reveal that current models struggle to robustly ground part concepts and predict actions in 3D space, and face challenges when manipulating object parts in long-horizon tasks.

