---
layout: default
title: Neural Decoding of Overt Speech from ECoG Using Vision Transformers and Contrastive Representation Learning
---

# Neural Decoding of Overt Speech from ECoG Using Vision Transformers and Contrastive Representation Learning

**arXiv**: [2512.04618v1](https://arxiv.org/abs/2512.04618) | [PDF](https://arxiv.org/pdf/2512.04618.pdf)

**作者**: Mohamed Baha Ben Ticha, Xingchen Ran, Guillaume Saldanha, Gaël Le Godais, Philémon Roussel, Marc Aubert, Amina Fontanell, Thomas Costecalde, Lucas Struber, Serpil Karakas, Shaomin Zhang, Philippe Kahane, Guillaume Charvet, Stéphan Chabardès, Blaise Yvert

---

## 💡 一句话要点

**提出基于视觉变换器和对比学习的编码器-解码器架构，用于从ECoG信号直接回归解码语音，以优化脑机接口中的语音重建。**

**关键词**: `语音脑机接口` `ECoG信号解码` `视觉变换器` `对比学习` `编码器-解码器架构` `无线植入系统`

## 📋 核心要点

1. 核心问题：从表面ECoG信号直接回归解码语音在流模式下仍具挑战，需优化神经解码器以提高性能。
2. 方法要点：集成视觉变换器和对比学习，增强ECoG信号到语音的直接回归，采用编码器-解码器深度神经网络架构。
3. 实验或效果：在两个数据集上评估，包括临床硬膜下电极和完全植入式无线硬膜外系统，为长期使用提供前景。

## 📄 摘要（原文）

> Speech Brain Computer Interfaces (BCIs) offer promising solutions to people with severe paralysis unable to communicate. A number of recent studies have demonstrated convincing reconstruction of intelligible speech from surface electrocorticographic (ECoG) or intracortical recordings by predicting a series of phonemes or words and using downstream language models to obtain meaningful sentences. A current challenge is to reconstruct speech in a streaming mode by directly regressing cortical signals into acoustic speech. While this has been achieved recently using intracortical data, further work is needed to obtain comparable results with surface ECoG recordings. In particular, optimizing neural decoders becomes critical in this case. Here we present an offline speech decoding pipeline based on an encoder-decoder deep neural architecture, integrating Vision Transformers and contrastive learning to enhance the direct regression of speech from ECoG signals. The approach is evaluated on two datasets, one obtained with clinical subdural electrodes in an epileptic patient, and another obtained with the fully implantable WIMAGINE epidural system in a participant of a motor BCI trial. To our knowledge this presents a first attempt to decode speech from a fully implantable and wireless epidural recording system offering perspectives for long-term use.

