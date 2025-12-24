---
layout: default
title: "MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments"
---

# MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21161" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21161v1</a>
  <a href="https://arxiv.org/pdf/2511.21161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21161v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21161v1', 'MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Hu, Yiyang Feng, Junran Peng, Jiawei He, Liyi Chen, Chuanchen Luo, Xucheng Yin, Qing Li, Zhaoxiang Zhang

**分类**: cs.RO

**发布日期**: 2025-11-26

**备注**: Project Page: https://xuhu0529.github.io/MarketGen

---

## 💡 一句话要点

**MarketGen：一个可扩展的具身智能超市环境自动生成仿真平台**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `具身智能` `仿真平台` `程序化内容生成` `超市环境` `机器人` `Sim-to-Real` `多模态输入`

## 📋 核心要点

1. 现有机器人数据集主要集中于家庭环境和短时任务，缺乏对复杂商业环境的支持，限制了具身智能在商业领域的应用。
2. MarketGen通过Agent驱动的程序化内容生成框架，支持多模态输入和真实世界设计原则，自动生成结构化、真实的超市环境。
3. 实验验证了MarketGen平台和基准测试的有效性，包括模块化Agent部署和Sim-to-Real迁移，为商业环境具身智能研究提供支持。

## 📝 摘要（中文）

本文提出了MarketGen，一个可扩展的仿真平台，能够自动生成复杂的超市环境，旨在解决现有机器人数据集和基准测试主要集中于家庭或桌面环境，以及短时任务的局限性。MarketGen采用了一种新颖的基于Agent的程序化内容生成（PCG）框架，该框架独特地支持多模态输入（文本和参考图像），并整合了真实世界的设计原则，以自动生成完整、结构化和真实的超市。此外，还提供了一个包含1100多种超市商品和参数化设施资产的广泛而多样的3D资产库。基于此，提出了一个新的超市Agent基准测试，包含两个日常任务：(1)收银台卸货：面向收银员Agent的长时程桌面任务；(2)货架商品收集：面向销售员Agent的复杂移动操作任务。通过大量实验验证了平台和基准测试，包括模块化Agent系统的部署和成功的Sim-to-Real迁移。MarketGen为加速复杂商业应用中具身智能的研究提供了一个全面的框架。

## 🔬 方法详解

**问题定义**：现有机器人数据集和基准测试主要集中于家庭或桌面环境，任务通常是短时程的，缺乏对复杂商业环境（如超市）的支持。这阻碍了具身智能Agent在商业领域的应用，例如，收银员辅助、商品整理等任务需要Agent在复杂环境中进行长时间的交互和操作。

**核心思路**：MarketGen的核心思路是利用程序化内容生成（PCG）技术，自动生成多样化、真实的超市环境。通过Agent驱动的PCG框架，可以根据文本描述和参考图像等多种模态的输入，自动生成超市的布局、商品摆放等细节。这种方法可以克服手动创建环境的成本高、效率低的问题，并能够生成大量不同的环境，用于训练和评估具身智能Agent。

**技术框架**：MarketGen的整体框架包含以下几个主要模块：1) Agent驱动的程序化内容生成模块：负责根据输入（文本、图像）自动生成超市环境；2) 3D资产库：包含大量超市商品和设施的3D模型，用于构建生成的环境；3) 仿真环境：提供物理引擎和传感器模拟，用于训练和评估Agent；4) 基准测试：定义了一系列超市环境中的任务，用于评估Agent的性能。

**关键创新**：MarketGen的关键创新在于其Agent驱动的程序化内容生成框架，该框架能够根据多模态输入（文本和参考图像）自动生成完整的、结构化的、真实的超市环境。与传统的PCG方法相比，MarketGen更加注重环境的结构化和真实性，并能够根据Agent的需求进行定制化生成。此外，MarketGen还提供了一个包含大量超市商品和设施的3D资产库，方便研究人员使用。

**关键设计**：MarketGen的Agent驱动的PCG框架采用了一种分层生成的方法，首先生成超市的整体布局，然后根据布局生成货架、商品等细节。在生成过程中，使用了大量的规则和约束，以保证生成环境的结构化和真实性。例如，货架的摆放需要符合超市的常见布局，商品的摆放需要符合商品的属性和销售策略。此外，MarketGen还提供了一系列参数化的设施资产，例如，可以调整货架的高度、宽度等参数，以生成不同类型的货架。

## 📊 实验亮点

实验结果表明，MarketGen平台生成的环境具有较高的真实性和多样性，能够有效地训练具身智能Agent。通过在MarketGen平台上训练的Agent，可以成功地完成收银台卸货和货架商品收集等任务。此外，实验还验证了Sim-to-Real迁移的可行性，将仿真环境中训练的Agent部署到真实超市中，取得了较好的效果。

## 🎯 应用场景

MarketGen平台可应用于训练和评估具身智能Agent在复杂商业环境中的能力，例如，收银员辅助Agent、商品整理Agent、顾客导购Agent等。该平台还可以用于研究Sim-to-Real迁移技术，将仿真环境中训练的Agent部署到真实超市中。此外，MarketGen还可以用于超市设计和规划，例如，评估不同布局对销售额的影响。

## 📄 摘要（原文）

> The development of embodied agents for complex commercial environments is hindered by a critical gap in existing robotics datasets and benchmarks, which primarily focus on household or tabletop settings with short-horizon tasks. To address this limitation, we introduce MarketGen, a scalable simulation platform with automatic scene generation for complex supermarket environments. MarketGen features a novel agent-based Procedural Content Generation (PCG) framework. It uniquely supports multi-modal inputs (text and reference images) and integrates real-world design principles to automatically generate complete, structured, and realistic supermarkets. We also provide an extensive and diverse 3D asset library with a total of 1100+ supermarket goods and parameterized facilities assets. Building on this generative foundation, we propose a novel benchmark for assessing supermarket agents, featuring two daily tasks in a supermarket: (1) Checkout Unloading: long-horizon tabletop tasks for cashier agents, and (2) In-Aisle Item Collection: complex mobile manipulation tasks for salesperson agents. We validate our platform and benchmark through extensive experiments, including the deployment of a modular agent system and successful sim-to-real transfer. MarketGen provides a comprehensive framework to accelerate research in embodied AI for complex commercial applications.

