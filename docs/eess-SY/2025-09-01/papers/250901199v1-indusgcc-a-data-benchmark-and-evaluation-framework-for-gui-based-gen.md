---
layout: default
title: "IndusGCC: A Data Benchmark and Evaluation Framework for GUI-Based General Computer Control in Industrial Automation"
---

# IndusGCC: A Data Benchmark and Evaluation Framework for GUI-Based General Computer Control in Industrial Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01199" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01199v1</a>
  <a href="https://arxiv.org/pdf/2509.01199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01199v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01199v1', 'IndusGCC: A Data Benchmark and Evaluation Framework for GUI-Based General Computer Control in Industrial Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoran Yang, Yuyang Du, Kexin Chen, Soung Chang Liew, Jiamin Lu, Ziyu Guo, Xiaoyan Liu, Qun Yang, Shiqi Xu, Xingyu Fan, Yuchen Pan, Taoyong Cui, Hongyu Deng, Boris Dudder, Jianzhang Pan, Qun Fang, Pheng Ann Heng

**分类**: eess.SY

**发布日期**: 2025-09-01

**🔗 代码/项目**: [GITHUB](https://github.com/Golden-Arc/IndustrialLLM)

---

## 💡 一句话要点

**IndusGCC：面向工业自动化GUI通用计算机控制的数据集与评估框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工业自动化` `通用计算机控制` `大型语言模型` `图形用户界面` `人机交互` `数据集` `评估框架`

## 📋 核心要点

1. 现有工业设备控制软件依赖GUI，需要人工交互，阻碍了基于代码的自动化。
2. 提出IndusGCC数据集和评估框架，利用LLM-GCC实现工业环境下的GUI自动化控制。
3. 实验表明LLM-GCC在工业自动化领域具有潜力，同时也面临着挑战，为未来研究奠定基础。

## 📝 摘要（中文）

随着工业4.0的发展，柔性制造已成为现代工业系统的基石，设备自动化在其中起着关键作用。然而，现有工业设备的控制软件通常依赖于图形用户界面（GUI），需要人工交互，例如鼠标点击或屏幕触摸，这给基于代码的设备自动化带来了重大障碍。最近，基于大型语言模型的通用计算机控制（LLM-GCC）已成为自动化基于GUI操作的一种有前景的方法。然而，工业环境带来了独特的挑战，包括视觉上多样化的、特定领域的界面以及需要高精度的关键任务。本文介绍了IndusGCC，这是第一个为工业环境中的LLM-GCC量身定制的数据集和基准，涵盖了七个领域的448个真实任务，从机器人手臂控制到生产线配置。IndusGCC具有与设备软件进行多模态人机交互的数据，为GUI级别的代码生成提供强大的监督。此外，我们提出了一个具有功能和结构指标的新型评估框架，以评估LLM生成的控制脚本。在主流LLM上的实验结果证明了LLM-GCC的潜力及其面临的挑战，为未来实现完全自动化工厂的研究奠定了坚实的基础。我们的数据和代码可在以下网址公开获取：https://github.com/Golden-Arc/IndustrialLLM。

## 🔬 方法详解

**问题定义**：论文旨在解决工业自动化领域中，现有控制软件依赖GUI导致自动化程度低的问题。现有方法需要人工操作GUI，效率低下且容易出错，无法满足柔性制造的需求。因此，如何利用代码自动控制GUI成为一个关键挑战。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大能力，通过学习人机交互数据，生成能够自动控制GUI的代码。这种方法将自然语言理解和代码生成相结合，使得用户可以通过自然语言指令来控制工业设备。

**技术框架**：IndusGCC框架包含数据集构建和评估框架两部分。数据集包含多模态人机交互数据，涵盖七个工业领域。评估框架则包含功能性和结构性指标，用于评估LLM生成的控制脚本的质量。整体流程是：首先，利用IndusGCC数据集训练LLM；然后，利用评估框架评估LLM生成的控制脚本的性能。

**关键创新**：该论文的关键创新在于构建了第一个面向工业自动化GUI控制的LLM-GCC数据集IndusGCC，并提出了相应的评估框架。与现有通用数据集不同，IndusGCC专注于工业领域，包含特定领域的界面和任务，更具实用价值。此外，评估框架不仅关注功能性，还关注代码的结构，能够更全面地评估LLM生成的代码质量。

**关键设计**：IndusGCC数据集包含多模态数据，例如屏幕截图、鼠标点击坐标、键盘输入等。评估框架包含功能性指标（例如任务完成率）和结构性指标（例如代码长度、代码复杂度）。论文还探索了不同的LLM模型，并针对工业自动化任务进行了微调。

## 📊 实验亮点

论文在主流LLM上进行了实验，结果表明LLM-GCC在工业自动化领域具有潜力。虽然现有LLM在IndusGCC数据集上的性能还有待提高，但实验结果为未来的研究方向提供了指导，例如如何更好地利用多模态数据、如何提高代码生成质量等。

## 🎯 应用场景

该研究成果可应用于各种工业自动化场景，例如机器人手臂控制、生产线配置、设备维护等。通过LLM-GCC，可以实现更灵活、高效的自动化生产，降低人工成本，提高生产效率。未来，该技术有望推动智能制造的发展，实现完全自动化工厂。

## 📄 摘要（原文）

> As Industry 4.0 progresses, flexible manufacturing has become a cornerstone of modern industrial systems, with equipment automation playing a pivotal role. However, existing control software for industrial equipment, typically reliant on graphical user interfaces (GUIs) that require human interactions such as mouse clicks or screen touches, poses significant barriers to the adoption of code-based equipment automation. Recently, Large Language Model-based General Computer Control (LLM-GCC) has emerged as a promising approach to automate GUI-based operations. However, industrial settings pose unique challenges, including visually diverse, domain-specific interfaces and mission-critical tasks demanding high precision. This paper introduces IndusGCC, the first dataset and benchmark tailored to LLM-GCC in industrial environments, encompassing 448 real-world tasks across seven domains, from robotic arm control to production line configuration. IndusGCC features multimodal human interaction data with the equipment software, providing robust supervision for GUI-level code generation. Additionally, we propose a novel evaluation framework with functional and structural metrics to assess LLM-generated control scripts. Experimental results on mainstream LLMs demonstrate both the potential of LLM-GCC and the challenges it faces, establishing a strong foundation for future research toward fully automated factories. Our data and code are publicly available at: \href{https://github.com/Golden-Arc/IndustrialLLM}{https://github.com/Golden-Arc/IndustrialLLM.

