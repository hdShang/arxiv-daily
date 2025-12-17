---
layout: default
title: BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation
---

# BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08572" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08572v1</a>
  <a href="https://arxiv.org/pdf/2510.08572.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08572v1" onclick="toggleFavorite(this, '2510.08572v1', 'BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rocktim Jyoti Das, Harsh Singh, Diana Turmakhan, Muhammad Abdullah Sohail, Mingfei Han, Preslav Nakov, Fabio Pizzati, Ivan Laptev

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-10-09

**备注**: 11 pages, 8 figures

---

## 💡 一句话要点

**BLAZER：利用零样本数据生成引导基于LLM的机器人操作代理**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `大型语言模型` `零样本学习` `数据生成` `模拟到真实迁移`

## 📋 核心要点

1. 机器人缺乏互联网规模的演示数据，现有数据集受限于手动收集和标注，规模较小。
2. BLAZER利用LLM的零样本能力在模拟环境中自动生成操作任务的演示数据，并用成功案例微调LLM。
3. 实验表明，BLAZER显著提升了模拟和真实环境中的零样本操作性能，并能泛化到训练集之外的任务。

## 📝 摘要（中文）

本文提出了BLAZER，一个通过自动生成训练数据来学习操作策略的框架。BLAZER利用LLM规划器的零样本能力，自动生成模拟环境中多样化操作任务的演示。成功的案例被用于微调LLM，从而在无需人工监督的情况下提升其规划能力。值得注意的是，虽然BLAZER的训练需要访问模拟器的状态，但研究表明，所获得的技能可以直接迁移到基于传感器的操作中。通过大量的实验，结果表明BLAZER显著提高了模拟和真实环境中零样本操作的性能，并且能够泛化到训练集之外的任务，同时还能实现LLM模型的降维。

## 🔬 方法详解

**问题定义**：现有机器人操作策略学习方法依赖于人工收集和标注的数据，数据规模有限，难以泛化到新的任务和环境。因此，如何高效地生成大规模、多样化的训练数据是关键问题。现有方法的痛点在于数据获取成本高昂，且难以覆盖所有可能的场景。

**核心思路**：BLAZER的核心思路是利用大型语言模型（LLM）的零样本能力，在模拟环境中自动生成操作任务的演示数据。通过让LLM规划器自主探索和解决任务，可以避免人工干预，从而大幅降低数据获取成本，并提高数据的多样性。

**技术框架**：BLAZER框架包含以下几个主要阶段：1) 使用LLM规划器在模拟环境中生成操作任务的演示数据；2) 筛选成功的演示案例，并用于微调LLM，提升其规划能力；3) 将训练好的策略迁移到真实机器人上进行操作。该框架的关键在于利用模拟器状态进行训练，然后实现到真实环境的迁移。

**关键创新**：BLAZER最重要的技术创新点在于利用LLM的零样本能力自动生成训练数据，从而避免了人工标注的需要。与现有方法相比，BLAZER能够更高效地获取大规模、多样化的训练数据，从而提升模型的泛化能力。此外，BLAZER还展示了将模拟环境中训练的策略直接迁移到真实机器人上的可行性。

**关键设计**：BLAZER的关键设计包括：1) 使用合适的LLM作为规划器，并设计有效的提示工程（prompt engineering）来引导LLM生成高质量的演示数据；2) 设计合适的奖励函数来筛选成功的演示案例；3) 使用行为克隆（behavior cloning）等方法来微调LLM，使其更好地学习操作策略；4) 采用域随机化（domain randomization）等技术来提高模型在真实环境中的鲁棒性。

## 📊 实验亮点

BLAZER在模拟和真实环境中都取得了显著的性能提升。在模拟环境中，BLAZER能够成功完成多种操作任务，并且能够泛化到训练集之外的任务。在真实环境中，BLAZER也能够成功地将模拟环境中学习到的策略迁移到真实机器人上，并完成相应的操作任务。实验结果表明，BLAZER显著提高了零样本操作的性能，并且能够实现LLM模型的降维。

## 🎯 应用场景

BLAZER具有广泛的应用前景，例如自动化装配、物流分拣、家庭服务机器人等领域。通过自动生成训练数据，可以大幅降低机器人部署的成本，并提高机器人的智能化水平。未来，BLAZER有望推动机器人技术在更多领域的应用，并促进人机协作的进一步发展。

## 📄 摘要（原文）

> Scaling data and models has played a pivotal role in the remarkable progress of computer vision and language. Inspired by these domains, recent efforts in robotics have similarly focused on scaling both data and model size to develop more generalizable and robust policies. However, unlike vision and language, robotics lacks access to internet-scale demonstrations across diverse robotic tasks and environments. As a result, the scale of existing datasets typically suffers from the need for manual data collection and curation. To address this problem, here we propose BLAZER, a framework that learns manipulation policies from automatically generated training data. We build on the zero-shot capabilities of LLM planners and automatically generate demonstrations for diverse manipulation tasks in simulation. Successful examples are then used to finetune an LLM and to improve its planning capabilities without human supervision. Notably, while BLAZER training requires access to the simulator's state, we demonstrate direct transfer of acquired skills to sensor-based manipulation. Through extensive experiments, we show BLAZER to significantly improve zero-shot manipulation in both simulated and real environments. Moreover, BLAZER improves on tasks outside of its training pool and enables downscaling of LLM models. Our code and data will be made publicly available on the project page.

