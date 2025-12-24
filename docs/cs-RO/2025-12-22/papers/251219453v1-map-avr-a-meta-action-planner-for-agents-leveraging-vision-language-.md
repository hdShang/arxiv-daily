---
layout: default
title: "MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation"
---

# MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19453" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19453v1</a>
  <a href="https://arxiv.org/pdf/2512.19453.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19453v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19453v1', 'MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenglong Guo, Yiming Zhao, Feng Jiang, Heng Jin, Zongbao Feng, Jianbin Zhou, Siyuan Xu

**分类**: cs.RO

**发布日期**: 2025-12-22

**备注**: 8 pages, 10 figures, This work was completed in December 2024

**🔗 代码/项目**: [PROJECT_PAGE](https://map-avr.github.io/)

---

## 💡 一句话要点

**MaP-AVR：结合视觉语言模型与检索增强生成，为机器人提出元动作规划器**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `机器人任务规划` `视觉语言模型` `检索增强生成` `元动作` `机器人技能学习` `上下文学习`

## 📋 核心要点

1. 现有具身机器人任务规划方法侧重于微调或CoT提示来增强LLM/VLM的任务理解能力，忽略了规划技能集定义的重要性。
2. 论文提出将规划结果抽象为元动作，包含机器人内在功能，而非人类中心概念，从而提高技能集的泛化能力。
3. 通过检索增强生成（RAG）技术，利用规划演示数据库进行上下文学习，确保LLM/VLM准确生成元动作格式，并在OmniGibson平台上验证了有效性。

## 📝 摘要（中文）

本文提出了一种名为MaP-AVR的元动作规划器，旨在提升具身机器人AI系统在复杂日常任务中的规划能力。该方法强调规划技能集的重要性，并提出将规划结果抽象为一组元动作，每个元动作包含{移动/旋转，末端执行器状态改变，与环境的关系}三个组成部分。这种抽象用机器人内在功能取代了以人为中心的动作概念，使规划结果与机器人可执行的动作范围对齐。为了确保LLM/VLM准确生成所需的元动作格式，采用了检索增强生成（RAG）技术，利用人工标注的规划演示数据库进行上下文学习。系统成功完成的任务越多，数据库将自我增强以支持多样性。使用GPT-4o和OmniGibson平台进行的实验表明，该方法与当前最先进的方法相比具有良好的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决具身机器人AI系统中，任务规划器在处理复杂日常任务时，由于技能集泛化能力不足而导致规划效果不佳的问题。现有方法通常侧重于增强LLM/VLM的任务理解能力，而忽略了规划技能集本身的设计，导致规划结果难以直接转化为机器人可执行的动作。

**核心思路**：论文的核心思路是将规划结果抽象为一组元动作，这些元动作基于机器人的内在功能（例如移动、旋转、末端执行器状态改变）来定义，而不是基于人类的动作概念（例如抓取、推动）。这种抽象提高了技能集的泛化能力，使得规划结果能够更好地适应不同的环境和任务。

**技术框架**：MaP-AVR 包含两个主要部分：元动作定义和检索增强生成（RAG）。首先，定义了一组元动作，每个元动作包含三个组成部分：{移动/旋转，末端执行器状态改变，与环境的关系}。然后，利用 RAG 技术，构建一个包含人工标注的规划演示数据库，在 LLM/VLM 生成元动作序列时，从数据库中检索相关的演示案例，以进行上下文学习，确保生成的元动作符合预期的格式和语义。随着系统完成更多任务，数据库会自我增强，不断提升系统的规划能力。

**关键创新**：该方法最重要的创新点在于提出了基于机器人内在功能的元动作抽象，以及将其与检索增强生成技术相结合。与现有方法相比，这种方法不再依赖于人类中心的概念来定义技能集，而是直接利用机器人的底层能力，从而提高了技能集的泛化能力和适应性。同时，RAG 技术的引入，使得 LLM/VLM 能够更好地理解和生成符合预期的元动作序列。

**关键设计**：元动作的设计是关键。每个元动作都由三个部分组成，这三个部分共同描述了机器人的一个基本操作。RAG 模块的关键在于数据库的构建和检索策略。数据库包含人工标注的规划演示案例，每个案例都包含任务描述和对应的元动作序列。检索策略需要能够根据当前的任务描述，从数据库中找到最相关的演示案例，以提供有效的上下文信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19453v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19453v1/meta-action-composed.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19453v1/task-extended-simple.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文使用GPT-4o作为LLM/VLM模型，并在OmniGibson平台上进行了实验验证。实验结果表明，MaP-AVR方法在任务规划方面表现出良好的性能，与当前最先进的方法相比具有竞争力。通过元动作抽象和RAG技术的结合，该方法能够生成更符合机器人能力的规划结果，并提高任务完成的成功率。具体性能数据和对比基线在论文中有详细描述。

## 🎯 应用场景

该研究成果可应用于各种需要机器人进行复杂任务规划的场景，例如家庭服务机器人、工业自动化机器人、医疗辅助机器人等。通过提高机器人的任务规划能力，可以使其更好地理解人类指令，完成各种日常任务，提高工作效率和生活质量。未来，该方法有望进一步扩展到更复杂的环境和任务中，实现更智能、更自主的机器人系统。

## 📄 摘要（原文）

> Embodied robotic AI systems designed to manage complex daily tasks rely on a task planner to understand and decompose high-level tasks. While most research focuses on enhancing the task-understanding abilities of LLMs/VLMs through fine-tuning or chain-of-thought prompting, this paper argues that defining the planned skill set is equally crucial. To handle the complexity of daily environments, the skill set should possess a high degree of generalization ability. Empirically, more abstract expressions tend to be more generalizable. Therefore, we propose to abstract the planned result as a set of meta-actions. Each meta-action comprises three components: {move/rotate, end-effector status change, relationship with the environment}. This abstraction replaces human-centric concepts, such as grasping or pushing, with the robot's intrinsic functionalities. As a result, the planned outcomes align seamlessly with the complete range of actions that the robot is capable of performing. Furthermore, to ensure that the LLM/VLM accurately produces the desired meta-action format, we employ the Retrieval-Augmented Generation (RAG) technique, which leverages a database of human-annotated planning demonstrations to facilitate in-context learning. As the system successfully completes more tasks, the database will self-augment to continue supporting diversity. The meta-action set and its integration with RAG are two novel contributions of our planner, denoted as MaP-AVR, the meta-action planner for agents composed of VLM and RAG. To validate its efficacy, we design experiments using GPT-4o as the pre-trained LLM/VLM model and OmniGibson as our robotic platform. Our approach demonstrates promising performance compared to the current state-of-the-art method. Project page: https://map-avr.github.io/.

