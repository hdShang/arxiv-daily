---
layout: default
title: "Apertus: Democratizing Open and Compliant LLMs for Global Language Environments"
---

# Apertus: Democratizing Open and Compliant LLMs for Global Language Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14233" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14233v2</a>
  <a href="https://arxiv.org/pdf/2509.14233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14233v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14233v2', 'Apertus: Democratizing Open and Compliant LLMs for Global Language Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Project Apertus, Alejandro Hernández-Cano, Alexander Hägele, Allen Hao Huang, Angelika Romanou, Antoni-Joan Solergibert, Barna Pasztor, Bettina Messmer, Dhia Garbaya, Eduard Frank Ďurech, Ido Hakimi, Juan García Giraldo, Mete Ismayilzada, Negar Foroutan, Skander Moalla, Tiancheng Chen, Vinko Sabolčec, Yixuan Xu, Michael Aerni, Badr AlKhamissi, Inés Altemir Mariñas, Mohammad Hossein Amani, Matin Ansaripour, Ilia Badanin, Harold Benoit, Emanuela Boros, Nicholas Browning, Fabian Bösch, Maximilian Böther, Niklas Canova, Camille Challier, Clement Charmillot, Jonathan Coles, Jan Deriu, Arnout Devos, Lukas Drescher, Daniil Dzenhaliou, Maud Ehrmann, Dongyang Fan, Simin Fan, Silin Gao, Miguel Gila, María Grandury, Diba Hashemi, Alexander Hoyle, Jiaming Jiang, Mark Klein, Andrei Kucharavy, Anastasiia Kucherenko, Frederike Lübeck, Roman Machacek, Theofilos Manitaras, Andreas Marfurt, Kyle Matoba, Simon Matrenok, Henrique Mendonça, Fawzi Roberto Mohamed, Syrielle Montariol, Luca Mouchel, Sven Najem-Meyer, Jingwei Ni, Gennaro Oliva, Matteo Pagliardini, Elia Palme, Andrei Panferov, Léo Paoletti, Marco Passerini, Ivan Pavlov, Auguste Poiroux, Kaustubh Ponkshe, Nathan Ranchin, Javi Rando, Mathieu Sauser, Jakhongir Saydaliev, Muhammad Ali Sayfiddinov, Marian Schneider, Stefano Schuppli, Marco Scialanga, Andrei Semenov, Kumar Shridhar, Raghav Singhal, Anna Sotnikova, Alexander Sternfeld, Ayush Kumar Tarun, Paul Teiletche, Jannis Vamvas, Xiaozhe Yao, Hao Zhao, Alexander Ilic, Ana Klimovic, Andreas Krause, Caglar Gulcehre, David Rosenthal, Elliott Ash, Florian Tramèr, Joost VandeVondele, Livio Veraldi, Martin Rajman, Thomas Schulthess, Torsten Hoefler, Antoine Bosselut, Martin Jaggi, Imanol Schlag

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-17 (更新: 2025-12-01)

---

## 💡 一句话要点

**Apertus：构建开放、合规且支持全球语言环境的大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `多语言` `数据合规` `开放模型` `预训练`

## 📋 核心要点

1. 现有开放LLM在数据合规性方面存在不足，常忽略内容所有者权利和隐私问题。
2. Apertus通过仅使用公开数据预训练，并追溯性地尊重robots.txt排除项来解决合规问题。
3. Apertus模型在多语言基准测试中表现出色，接近或超过其他开放权重模型，并开源所有开发资源。

## 📝 摘要（中文）

本文介绍了Apertus，一套完全开放的大语言模型（LLM），旨在解决当前开放模型生态系统中的两个系统性缺陷：数据合规性和多语言表示。与许多在未提供可复现数据流程或未考虑内容所有者权利的情况下发布权重的模型不同，Apertus模型仅在公开可用的数据上进行预训练，追溯性地尊重`robots.txt`排除项，并过滤非许可、有害和个人身份信息内容。为了降低记忆风险，我们在预训练期间采用了Goldfish目标，强烈抑制数据的逐字回忆，同时保持下游任务的性能。Apertus模型还扩展了多语言覆盖范围，在来自1800多种语言的15T tokens上进行训练，其中约40%的预训练数据分配给非英语内容。Apertus模型以8B和70B规模发布，在多语言基准测试中接近完全开放模型的最新结果，与开放权重模型相媲美或超越。除了模型权重外，我们还发布了开发周期中的所有科学成果，包括数据准备脚本、检查点、评估套件和训练代码，并采用宽松的许可证，从而实现透明的审计和扩展。

## 🔬 方法详解

**问题定义**：当前开源大语言模型生态面临数据合规性和多语言支持不足的问题。许多模型在训练数据来源上不够透明，可能侵犯版权或包含有害信息。同时，对非英语语言的支持也相对有限，无法满足全球用户的需求。

**核心思路**：Apertus的核心思路是构建一个完全开放、合规且支持广泛语言的大语言模型。通过严格筛选训练数据，确保其来源合法且不包含有害内容。同时，通过增加非英语数据的比例，提升模型在多语言环境下的表现。

**技术框架**：Apertus的训练流程主要包括以下几个阶段：1) 数据收集与清洗：从公开渠道收集数据，并根据robots.txt排除项进行过滤，移除有害和个人身份信息内容。2) 预训练：使用收集到的数据对模型进行预训练，采用Goldfish目标来抑制记忆效应。3) 评估：使用多语言基准测试评估模型的性能。4) 发布：发布模型权重、数据准备脚本、检查点、评估套件和训练代码。

**关键创新**：Apertus的关键创新在于其对数据合规性的重视和对多语言支持的扩展。通过严格的数据筛选和Goldfish目标，降低了模型记忆和生成有害内容的风险。同时，通过增加非英语数据的比例，提升了模型在多语言环境下的表现。

**关键设计**：Apertus采用了Goldfish目标作为预训练的正则化方法，旨在减少模型对训练数据的过度记忆。具体来说，Goldfish目标鼓励模型生成与输入文本相似但又不完全相同的文本，从而降低了逐字回忆的风险。此外，Apertus在训练数据中分配了约40%的比例给非英语内容，以提升模型的多语言能力。

## 📊 实验亮点

Apertus模型在多语言基准测试中取得了与现有开放权重模型相媲美甚至超越的性能。例如，在某些多语言任务上，Apertus 70B模型接近了最先进的开放模型，同时保证了数据合规性和透明度。此外，开源所有开发资源也为社区提供了极大的便利。

## 🎯 应用场景

Apertus可应用于机器翻译、跨语言信息检索、多语言内容生成等领域。其开放性和合规性使其更易于被研究人员和开发者采用，促进全球语言环境下的AI应用发展。未来，Apertus有望成为构建负责任、可信赖的AI系统的基础模型。

## 📄 摘要（原文）

> We present Apertus, a fully open suite of large language models (LLMs) designed to address two systemic shortcomings in today's open model ecosystem: data compliance and multilingual representation. Unlike many prior models that release weights without reproducible data pipelines or regard for content-owner rights, Apertus models are pretrained exclusively on openly available data, retroactively respecting `robots.txt` exclusions and filtering for non-permissive, toxic, and personally identifiable content. To mitigate risks of memorization, we adopt the Goldfish objective during pretraining, strongly suppressing verbatim recall of data while retaining downstream task performance. The Apertus models also expand multilingual coverage, training on 15T tokens from over 1800 languages, with ~40% of pretraining data allocated to non-English content. Released at 8B and 70B scales, Apertus approaches state-of-the-art results among fully open models on multilingual benchmarks, rivalling or surpassing open-weight counterparts. Beyond model weights, we release all scientific artifacts from our development cycle with a permissive license, including data preparation scripts, checkpoints, evaluation suites, and training code, enabling transparent audit and extension.

