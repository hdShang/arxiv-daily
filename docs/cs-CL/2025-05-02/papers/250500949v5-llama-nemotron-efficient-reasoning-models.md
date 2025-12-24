---
layout: default
title: "Llama-Nemotron: Efficient Reasoning Models"
---

# Llama-Nemotron: Efficient Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00949" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00949v5</a>
  <a href="https://arxiv.org/pdf/2505.00949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00949v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00949v5', 'Llama-Nemotron: Efficient Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akhiad Bercovich, Itay Levy, Izik Golan, Mohammad Dabbah, Ran El-Yaniv, Omri Puny, Ido Galil, Zach Moshe, Tomer Ronen, Najeeb Nabwani, Ido Shahaf, Oren Tropp, Ehud Karpas, Ran Zilberstein, Jiaqi Zeng, Soumye Singhal, Alexander Bukharin, Yian Zhang, Tugrul Konuk, Gerald Shen, Ameya Sunil Mahabaleshwarkar, Bilal Kartal, Yoshi Suhara, Olivier Delalleau, Zijia Chen, Zhilin Wang, David Mosallanezhad, Adi Renduchintala, Haifeng Qian, Dima Rekesh, Fei Jia, Somshubra Majumdar, Vahid Noroozi, Wasi Uddin Ahmad, Sean Narenthiran, Aleksander Ficek, Mehrzad Samadi, Jocelyn Huang, Siddhartha Jain, Igor Gitman, Ivan Moshkov, Wei Du, Shubham Toshniwal, George Armstrong, Branislav Kisacanin, Matvei Novikov, Daria Gitman, Evelina Bakhturina, Prasoon Varshney, Makesh Narsimhan, Jane Polak Scowcroft, John Kamalu, Dan Su, Kezhi Kong, Markus Kliegl, Rabeeh Karimi Mahabadi, Ying Lin, Sanjeev Satheesh, Jupinder Parmar, Pritam Gundecha, Brandon Norick, Joseph Jennings, Shrimai Prabhumoye, Syeda Nahida Akter, Mostofa Patwary, Abhinav Khattar, Deepak Narayanan, Roger Waleffe, Jimmy Zhang, Bor-Yiing Su, Guyue Huang, Terry Kong, Parth Chadha, Sahil Jain, Christine Harvey, Elad Segal, Jining Huang, Sergey Kashirsky, Robert McQueen, Izzy Putterman, George Lam, Arun Venkatesan, Sherry Wu, Vinh Nguyen, Manoj Kilaru, Andrew Wang, Anna Warno, Abhilash Somasamudramath, Sandip Bhaskar, Maka Dong, Nave Assaf, Shahar Mor, Omer Ullman Argov, Scot Junkin, Oleksandr Romanenko, Pedro Larroy, Monika Katariya, Marco Rovinelli, Viji Balas, Nicholas Edelman, Anahita Bhiwandiwalla, Muthu Subramaniam, Smita Ithape, Karthik Ramamoorthy, Yuting Wu, Suguna Varshini Velury, Omri Almog, Joyjit Daw, Denys Fridman, Erick Galinkin, Michael Evans, Shaona Ghosh, Katherine Luna, Leon Derczynski, Nikki Pope, Eileen Long, Seth Schneider, Guillermo Siman, Tomasz Grzegorzek, Pablo Ribalta, Monika Katariya, Chris Alexiuk, Joey Conway, Trisha Saar, Ann Guan, Krzysztof Pawelec, Shyamala Prayaga, Oleksii Kuchaiev, Boris Ginsburg, Oluwatobi Olabiyi, Kari Briski, Jonathan Cohen, Bryan Catanzaro, Jonah Alben, Yonatan Geifman, Eric Chung

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-02 (更新: 2025-09-09)

---

## 💡 一句话要点

**提出Llama-Nemotron系列模型以提升推理效率与能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `推理模型` `动态推理切换` `知识蒸馏` `大规模强化学习` `开源模型`

## 📋 核心要点

1. 现有推理模型在推理效率和内存使用上存在不足，难以满足企业级应用需求。
2. Llama-Nemotron系列模型通过异构设计和动态推理切换，提升了推理能力和效率，支持企业使用。
3. 与最先进的DeepSeek-R1模型相比，Llama-Nemotron在推理吞吐量和内存效率上表现更佳。

## 📝 摘要（中文）

我们介绍了Llama-Nemotron系列模型，这是一个开放的异构推理模型家族，具备卓越的推理能力和高效的推理性能，并允许企业使用。该系列模型分为三种规模——Nano（8B）、Super（49B）和Ultra（253B），在推理吞吐量和内存效率上优于现有的最先进推理模型DeepSeek-R1。本文讨论了这些模型的训练过程，包括使用Llama 3模型的神经架构搜索、知识蒸馏和持续预训练，随后进行以推理为重点的后训练阶段，包含监督微调和大规模强化学习。Llama-Nemotron模型是首个支持动态推理切换的开源模型，用户可以在推理过程中在标准聊天和推理模式之间切换。为了支持开放研究和模型开发，我们发布了Llama-Nemotron推理模型及其完整的后训练数据集和训练代码库。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有推理模型在推理效率和内存使用上的不足，尤其是在企业应用场景中的挑战。现有方法往往无法在保证推理能力的同时，提供足够的效率和灵活性。

**核心思路**：Llama-Nemotron系列模型通过异构设计和动态推理切换，允许用户在标准聊天和推理模式之间灵活切换，从而提升推理能力和效率。该设计使得模型能够在不同任务中自适应调整，满足多样化的应用需求。

**技术框架**：整体架构包括三个主要阶段：首先是使用Llama 3模型进行神经架构搜索以加速推理；其次是知识蒸馏和持续预训练；最后是推理聚焦的后训练阶段，包含监督微调和大规模强化学习。

**关键创新**：Llama-Nemotron模型的最大创新在于其动态推理切换功能，使其成为首个支持此功能的开源推理模型，显著提升了用户在推理过程中的灵活性和效率。

**关键设计**：在训练过程中，采用了多种技术细节，包括特定的损失函数和网络结构设计，以确保模型在推理时的高效性和准确性。具体的参数设置和训练策略也经过精心设计，以优化模型性能。

## 📊 实验亮点

在与DeepSeek-R1的对比实验中，Llama-Nemotron系列模型在推理吞吐量和内存效率上均表现出显著提升，尤其是Ultra版本在处理复杂推理任务时展现了更高的性能，具体数据未披露。

## 🎯 应用场景

Llama-Nemotron系列模型具有广泛的应用潜力，尤其适用于需要高效推理的企业级应用场景，如智能客服、数据分析和决策支持系统等。其开放的许可协议也为研究人员和开发者提供了便利，促进了模型的进一步开发和应用。

## 📄 摘要（原文）

> We introduce the Llama-Nemotron series of models, an open family of heterogeneous reasoning models that deliver exceptional reasoning capabilities, inference efficiency, and an open license for enterprise use. The family comes in three sizes -- Nano (8B), Super (49B), and Ultra (253B) -- and performs competitively with state-of-the-art reasoning models such as DeepSeek-R1 while offering superior inference throughput and memory efficiency. In this report, we discuss the training procedure for these models, which entails using neural architecture search from Llama 3 models for accelerated inference, knowledge distillation, and continued pretraining, followed by a reasoning-focused post-training stage consisting of two main parts: supervised fine-tuning and large scale reinforcement learning. Llama-Nemotron models are the first open-source models to support a dynamic reasoning toggle, allowing users to switch between standard chat and reasoning modes during inference. To further support open research and facilitate model development, we provide the following resources: 1. We release the Llama-Nemotron reasoning models -- LN-Nano, LN-Super, and LN-Ultra -- under the commercially permissive NVIDIA Open Model License Agreement. 2. We release the complete post-training dataset: Llama-Nemotron-Post-Training-Dataset. 3. We also release our training codebases: NeMo, NeMo-Aligner, and Megatron-LM.

